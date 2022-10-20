#%%
from dataclasses import dataclass
from typing import Iterator
import pandas as pd
import zoom_api

@dataclass(frozen=True)
class MeetingRegistrants:
    meeting: pd.DataFrame
    registrants: pd.DataFrame



def list_registrants(
    token: str, 
    from_date='2022-10-10', 
    to_date='2022-10-14',
    ) -> Iterator[MeetingRegistrants]:
    """
    """

    user_df = pd.DataFrame(zoom_api.list_users(token=token))
    owner_id = user_df[user_df.role_id == '0'].iloc[-1].id
    meetings = pd.DataFrame(zoom_api.list_meetings2(token=token, user_id=owner_id, from_=from_date, to=to_date))
    for meeting_id, meeting in meetings.groupby('id'):
        registrants = pd.DataFrame(zoom_api.list_registrants(token=token, meeting_id=meeting_id))
        
        meeting_registrants = MeetingRegistrants(
            meeting=meeting,
            registrants=registrants,
        )
        yield meeting_registrants


#%%
credentials = zoom_api.Credentials.from_environment_variables()
oauth = credentials.get_oauth()
token = oauth["access_token"]

registrants_iterator = list_registrants(
    token=token,
    from_date='2022-10-10',
    to_date='2022-12-25',
)
#%%

for meeting_registrants in registrants_iterator:
    meeting = meeting_registrants.meeting
    registrants = meeting_registrants.registrants
    print(f"----------{meeting.id[0]}---------")
    print(meeting[['id', 'uuid', 'topic', 'start_time']], end='\n\n')
    print(registrants[['first_name', 'last_name', 'email', 'create_time']], end='\n\n')
    print('')

