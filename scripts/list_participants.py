import pandas as pd
import zoom_api


# Use Case: Get Participation
from_date = '2022-10-10'
to_date = '2022-10-14'

creds = zoom_api.Credentials.from_environment_variables()
oauth = zoom_api.get_server2server_oauth(
    account_id=creds.zoom_account_id,
    client_id=creds.zoom_client_id,
    client_secret=creds.zoom_client_secret,
)
token = oauth["access_token"]

user_df = pd.DataFrame(zoom_api.list_users(token=token))
owner_id = user_df[user_df.role_id == '0'].iloc[-1].id
print(owner_id)

meetings = pd.DataFrame(zoom_api.list_meetings2(token=token, user_id=owner_id, from_=from_date, to=to_date))
print(meetings)

unique_meeting_ids = meetings.id.unique()
print(unique_meeting_ids)


for meeting_uuid in meetings.uuid[0:1]:
    print(f'Participants for meeting {meeting_uuid}:')
    print(pd.DataFrame(zoom_api.get_meeting_participant_events(token=token, meeting_id=meeting_uuid)))
