from __future__ import annotations

from functools import lru_cache
from typing import TypedDict, List

import requests


class Meeting2(TypedDict):
    uuid: str
    id: int
    host_id: str
    type: int
    topic: str
    user_name: str
    user_email: str
    start_time: str
    end_time: str
    duration: int
    total_minutes: int
    participants_count: int
    source: str

@lru_cache()
def list_meetings2(token: str, user_id, from_: str, to: str, type='past'):
    """
    GET /report/users/{userId}/meetings
    https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/reportMeetings

    Attributes:
        from_: str = YYYY-MM-DD
        to: str = YYYY-MM-DD
    """
    class ReportUserMeetingsResponse(TypedDict):
        from_: str
        to: str
        total_records: int
        page_size: int
        page_count: int
        next_page_token: str
        meetings: List[Meeting2]

    resp = requests.get(
        f"https://api.zoom.us/v2/report/users/{user_id}/meetings?from={from_}&to={to}&type={type}",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert resp.content
    data: ReportUserMeetingsResponse = resp.json()
    return data['meetings']
