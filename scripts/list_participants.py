from typing import Iterator, List, Dict, Tuple
from pathlib import Path
import pandas as pd

import zoom_api


def list_participants(token, from_date, to_date) -> Iterator[pd.DataFrame]:
    user_df = pd.DataFrame(zoom_api.list_users(token=token))
    owner_id = user_df[user_df.role_id == '0'].iloc[-1].id
    meetings = zoom_api.list_past_meeting_sessions(token=token, user_id=owner_id, from_=from_date, to=to_date)

    for meeting in meetings:
        events = pd.DataFrame(zoom_api.get_meeting_participant_events(token=token, meeting_id=meeting['uuid']))
        for key, value in meeting.items():
            events['meeting_' + key] = value
        yield events


if __name__ == '__main__':
    creds = zoom_api.Credentials.from_environment_variables()
    oauth = zoom_api.get_server2server_oauth(
        account_id=creds.zoom_account_id,
        client_id=creds.zoom_client_id,
        client_secret=creds.zoom_client_secret,
    )

    basedir = Path('data')
    basedir.mkdir(parents=True, exist_ok=True)
    for meeting_events in list_participants(token=(oauth["access_token"]), from_date='2022-10-24', to_date='2022-10-28'):
        meeting_events.to_csv(basedir / ('attendance_' + meeting_events['meeting_start_time'].iloc[0] + '.csv'))
        print(len(meeting_events))

