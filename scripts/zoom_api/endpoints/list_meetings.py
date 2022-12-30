from __future__ import annotations

from _warnings import warn
from functools import lru_cache
from typing import TypedDict, List, Optional, Literal

import requests


class Meeting(TypedDict):
    uuid: str
    id: int
    host_id: str
    topic: str
    type: int
    start_time: str
    duration: int
    timezone: str
    agenda: str
    created_at: str
    join_url: str


def list_meetings(
    token: str,
    user_id="me", 
    page_size: int = 100, 
    type: Literal['scheduled', 'live', 'upcoming', 'upcoming_meetings', 'previous_meetings'] = 'scheduled',
    ) -> List[Meeting]:
    """
    GET /users/{userId}/meetings
    https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetings
    """
    class MeetingResponse(TypedDict):
        page_size: int
        total_records: int
        next_page_token: Optional[str]
        meetings: List[Meeting]

    resp = requests.get(
        f"https://api.zoom.us/v2/users/{user_id}/meetings?page_size={page_size}&type={type}",
        headers={"Authorization": f"Bearer {token}"}
    )

    data: MeetingResponse = resp.json()
    if data['page_size'] < data['total_records']:
        warn(f"Only extracting {data['page_size']} of {data['total_records']} meetings")

    meetings = data["meetings"]
    return meetings



