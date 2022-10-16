import pandas as pd
import zoom_api


def list_registrants(token, from_date, to_date):
    user_df = pd.DataFrame(zoom_api.list_users(token=token))
    owner_id = user_df[user_df.role_id == '0'].iloc[-1].id
    meetings = pd.DataFrame(zoom_api.list_meetings2(token=token, user_id=owner_id, from_=from_date, to=to_date))
    unique_meeting_ids = meetings.id.unique()
    for meeting_id in unique_meeting_ids:
        print(pd.DataFrame(zoom_api.list_registrants(token=token, meeting_id=meeting_id)))


if __name__ == '__main__':
    creds = zoom_api.Credentials.from_environment_variables()
    oauth = zoom_api.get_server2server_oauth(
        account_id=creds.zoom_account_id,
        client_id=creds.zoom_client_id,
        client_secret=creds.zoom_client_secret,
    )
    list_registrants(
        token=(oauth["access_token"]),
        from_date='2022-10-10',
        to_date='2022-10-14',
    )
