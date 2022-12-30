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
        from_=(today - timedelta(days=70)).strftime("%Y-%m-%d"), 
        to=today.strftime("%Y-%m-%d"),
    )
    past_meetings.extend(courses)



# %%
len(past_meetings)

# %%
pd.DataFrame(past_meetings)

# %% [markdown]
# ### Keep only the Recurring, Fixed Time Meetings (the ones that indicate a course was done)

# %%
is_recurringfixed = lambda m: zoom_api.meeting_type_is(m, zoom_api.MeetingType.RecurringFixedTime)
past_courses = pd.DataFrame(list(filter(is_recurringfixed, past_meetings)))
past_courses.head()

# %% [markdown]
# ### Group each session into the course it belongs to, then save those sessions to file.
#  
# Make two Files:
#   - One for each session's info
#   - one for the info that stays consistent across the course (for easier querying)

# %%
from pathlib import Path
folder = Path('data/courses')
for id, course in past_courses.groupby('id'):
    topic = course.topic.iloc[0]
    start_time = parse(course['start_time'].min()).astimezone(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%d %H:%M')
    jsonized_data = json.dumps(course.to_dict('records'), indent=4)
    course_folder = folder / f"{start_time} {topic}"
    print(course_folder)
    course_folder.mkdir(exist_ok=True, parents=True)
    (course_folder / "sessions.json").write_text(jsonized_data)

    course_info = course[['id', 'type', 'topic', 'user_name', 'user_email', 'source']].iloc[0].to_dict()
    for col in course_info:
        assert len(course[col].unique()) == 1
    (course_folder / "course.json").write_text(json.dumps(course_info, indent=4))

    


# %% [markdown]
# # Part 2: Get Registrants for each Course

# %%
for id, course in past_courses.groupby('id'):
    regs = pd.DataFrame(zoom_api.list_registrants(token=token, meeting_id=course.iloc[0]['id']))
    regs = regs.drop(columns=['address', 'city', 'country', 'zip', 'state', 'phone', 'industry', 'purchasing_time_frame', 'role_in_purchase_process', 'no_of_employees'])
    regs = regs[::-1].reset_index(drop=True) # organize first-to-last to register
    regs.index += 1  # index from 1, to count number of registrants

    # Get course folder to save data in
    topic = course.topic.iloc[0]
    start_time = parse(course['start_time'].min()).astimezone(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%d %H:%M')
    course_folder = folder / f"{start_time} {topic}"
    print(course_folder)

    # Save machine-readable version with data for analysis
    jsonized_data = json.dumps(regs.to_dict('records'), indent=4)
    (course_folder / "registrations.json").write_text(jsonized_data)
    print('done')

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


    
    
    

# %% [markdown]
# ## Part 3: Get Participation

# %% [markdown]
# ### Download all Participant Events

# %%
for id, course in past_courses.groupby('id'):
    # Get course folder to save data in
    topic = course.topic.iloc[0]
    start_time = parse(course['start_time'].min()).astimezone(pytz.timezone('Europe/Berlin')).strftime('%Y-%m-%d %H:%M')
    course_folder = folder / f"{start_time} {topic}" / "participation_events"
    course_folder.mkdir(exist_ok=True, parents=True)
    
    for uuid, session in course.groupby('uuid'):
        # Save Data
        parts = zoom_api.get_meeting_participant_events(token=token, meeting_id=session['uuid'].iloc[0])
        filename = parse(session['start_time'].iloc[0]).strftime("%Y-%m-%d %H:%M") \
            + parse(session['end_time'].iloc[0]).strftime("-%H:%M") \
            + '.json'

        print(course_folder / filename)
        (course_folder / filename).write_text(json.dumps(parts, indent=4))

    

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




