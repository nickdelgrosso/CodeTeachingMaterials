from __future__ import annotations

from typing import TypedDict, List

import requests


class ActiveUser(TypedDict):
    id: str
    email: str
    user_name: str
    type: int
    dept: str
    meetings: int
    participants: int
    meeting_minutes: int
    last_client_version: str
    last_login_time: str
    create_time: str


def get_active_hosts(token: str, from_date: str = "2022-10-14", to_date: str = "2022-10-15") -> List[ActiveUser]:

    class ActiveUsersReportResponse(TypedDict):
        # 'from': str
        to: str
        page_count: int
        page_number: int
        page_size: int
        total_records: int
        next_page_token: str
        total_meetings: int
        total_participants: int
        total_meeting_minutes: int
        users: List[ActiveUser]

    resp = requests.get(
        f"https://api.zoom.us/v2/report/users",
        # f"https://api.zoom.us/v2/report/meetings/{meeting_id}",
        headers = {"Authorization": f"Bearer {token}"},
        params={
            'type': 'active',
            'from': from_date,
            'to': to_date,
            'page_size': 100,
        }
    )
    assert resp.content
    data: ActiveUsersReportResponse = resp.json()
    return data['users']
