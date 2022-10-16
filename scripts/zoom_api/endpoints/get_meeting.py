import requests




def get_meeting(token: str, meeting_id: str):
    """
    GET
    https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meeting
    """
    raise NotImplementedError("Not yet implemented")
    resp = requests.get(
        f"https://api.zoom.us/v2/meetings/{meeting_id}",
        headers={"Authorization": f"Bearer {token}"}
    )

    data = resp.json()
    if data['page_size'] < data['total_records']:
        warn(f"Only extracting {data['page_size']} of {data['total_records']} meetings")


