#%%
from dataclasses import dataclass
from typing import Iterator
import pandas as pd
from pathlib import Path
import zoom_api
from tabulate import tabulate

@dataclass(frozen=True)
class MeetingRegistrants:
    meeting: pd.DataFrame
    registrants: pd.DataFrame



def list_upcoming_registrants(token: str) -> Iterator[MeetingRegistrants]:
    """
    """
    meetings = pd.DataFrame(zoom_api.list_meetings(token=token, type='upcoming'))
    
    for meeting_id, meeting in meetings.sort_values('start_time', ascending=False).groupby('id'):
        try:
            regs = zoom_api.list_registrants(token=token, meeting_id=meeting_id)
        except ValueError as exc:
            if 'Registration has not been enabled' in str(exc):
                continue
            else:
                raise exc

        registrants = pd.DataFrame(regs)
        registrants.index += 1  # shift registration count by 1, for easier visual counting
        
        meeting_registrants = MeetingRegistrants(
            meeting=meeting,
            registrants=registrants,
        )
        yield meeting_registrants


#%%
credentials = zoom_api.Credentials.from_environment_variables()
oauth = credentials.get_oauth()
token = oauth["access_token"]

registrants_iterator = list_upcoming_registrants(token=token)
#%%

for meeting_registrants in registrants_iterator:
    meeting = meeting_registrants.meeting
    registrants = meeting_registrants.registrants
    print(f"----------{meeting.id.iloc[0]}---------")
    print(meeting[['id', 'uuid', 'topic', 'start_time']], end='\n\n')
    # print(registrants[['first_name', 'last_name', 'email', 'create_time']], end='\n\n')
    # regs = registrants[['last_name', 'first_name', 'create_time']].sort_values('create_time').reset_index(drop=True)
    regs = registrants[['first_name', 'last_name', 'create_time']].sort_values('create_time', ascending=False).reset_index(drop=True)
    regs.index += 1
    output = tabulate(regs, headers='keys', tablefmt='psql')
    print(output, end='\n\n')
    print('')

    filename = Path('/home/nickdg/Dropbox/Teaching/Registrants') / (str(meeting.id.iloc[0]) + '.txt')
    filename.touch(exist_ok = True)
    with filename.open(mode='r+') as f:
        f.write(output)

    # print(regs, end='\n\n')
    
