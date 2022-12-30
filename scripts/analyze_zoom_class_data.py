# %%

# import os
# os.chdir('..')

# %%
import zoom_api
from datetime import datetime, timedelta
import pandas as pd
from dateutil.parser import parse
import json
import pytz
from utils.email import to_mailbox

# %%
oauth = zoom_api.Credentials.from_environment_variables().get_oauth()
token = oauth['access_token']
assert token

# %% [markdown]
# ### Get All Past Meetings by the Teachers

# %%
past_meetings = []
for teacher in zoom_api.list_users(token=token, role_id=0):
    today = datetime.today()
    courses = zoom_api.get_all_meeting_reports(
        token=token, 
        user_id=teacher["id"], 
        from_=(today - timedelta(days=100)).strftime("%Y-%m-%d"), 
        to=today.strftime("%Y-%m-%d"),
    )
    past_meetings.extend(courses)


past_meetings = pd.DataFrame(past_meetings)


# %% Keep only the Recurring, Fixed Time Meetings (the ones that indicate a course was done)
past_courses = past_meetings.query('type == 8')
past_courses

# %%
# Make Labels for each course id, for making folder names
course_labels = {}
for id, course in past_courses.groupby('id'):
    topic = course.topic.iloc[0]
    start_time = parse(course['start_time'].min()).astimezone(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%d')
    jsonized_data = json.dumps(course.to_dict('records'), indent=4)
    label = f"{start_time} {topic} {id}"
    course_labels[id] = label
course_labels


# %% Write Course Info and Session Info
from pathlib import Path
folder = Path('data/courses')
for id, course in past_courses.groupby('id'):

    course_folder = folder / course_labels[id]
    course_folder.mkdir(exist_ok=True, parents=True)

    # Write all Course Data to JSON File
    jsonized_data = json.dumps(course.to_dict('records'), indent=4)
    (course_folder / "sessions.json").write_text(jsonized_data)

    # Write Only the Repeated Course Data to Another File, for easier human reading
    course_info = course[['id', 'type', 'topic', 'user_name', 'user_email', 'source']].iloc[0].to_dict()
    for col in course_info:
        assert len(course[col].unique()) == 1
    (course_folder / "course.json").write_text(json.dumps(course_info, indent=4))

    

# %% Get Registrants for each Course
for id, course in past_courses.groupby('id'):
    regs = pd.DataFrame(zoom_api.list_registrants(token=token, meeting_id=id))
    regs = regs.drop(columns=['address', 'city', 'country', 'zip', 'state', 'phone', 'industry', 'purchasing_time_frame', 'role_in_purchase_process', 'no_of_employees'])
    regs = regs[::-1].reset_index(drop=True) # organize first-to-last to register
    regs.index += 1  # index from 1, to count number of registrants

    # Get course folder to save data in
    course_folder = folder / course_labels[id]

    # Save machine-readable version with data for analysis
    jsonized_data = json.dumps(regs.to_dict('records'), indent=4)
    (course_folder / "registrations.json").write_text(jsonized_data)
    

    # Save human-readable summary for counting people, communicating with coordinators
    regs2 = pd.DataFrame(index=regs.index).assign(**{
        'Last Name': regs['last_name'],
        'First Name': regs['first_name'],
        'Email': regs['email'],
        'Registration Time': pd.to_datetime(regs.create_time).dt.tz_convert('Europe/Berlin').dt.strftime('%Y-%m-%d %H:%M'),
    })
    regs2.to_csv(course_folder / "registrations.csv")
    
    # Make copy-pastable version for batch emailing
    mailboxes = [to_mailbox(r['email'], r.get('first_name'), r.get('last_name')) for i, r in regs.iterrows()]
    (course_folder / "registrant_emails.txt").write_text('\n'.join(mailboxes) + '\n')
    

# %% Get Raw Participation Events Data at Each Session
for id, course in past_courses.groupby('id'):
    
    course_folder = folder / course_labels[id] / "participation_events"
    course_folder.mkdir(exist_ok=True, parents=True)
    
    for uuid, session in course.groupby('uuid'):
        # Save Data
        parts = zoom_api.get_meeting_participant_events(token=token, meeting_id=session['uuid'].iloc[0])
        filename = parse(session['start_time'].iloc[0]).strftime("%Y-%m-%d %H:%M") \
            + parse(session['end_time'].iloc[0]).strftime("-%H:%M") \
            + '.json'

        filepath = course_folder / filename
        filepath.write_text(json.dumps(parts, indent=4))
        print(filepath)

    

# %% [markdown]
# ### Process the Events to calculate Attendance

# %%
for course_folder in Path('data/courses').glob('*/'):

    # Read in all participation events from a course into a single DataFrame
    filenames = list(course_folder.glob('participation_events/*.json'))
    df = pd.concat([pd.read_json(f) for f in filenames], ignore_index=True)

    # Calculate Attendance by adding up the durations, grouped by name and user email (note that the names and emails may have errors)
    attendance = (df.groupby(['name', 'user_email', df.join_time.dt.strftime('%Y-%m-%d')]).duration.sum() / 60**2).round(1).unstack()

    # Save the data
    attendance.to_csv(course_folder / 'attendance.csv')
    attendance.to_excel(course_folder / 'attendance.xlsx')





# %%
