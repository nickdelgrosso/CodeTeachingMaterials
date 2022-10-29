from __future__ import annotations

import urllib.parse
from functools import lru_cache
from typing import List, Optional, TypedDict

import requests


class ParticipantReport(TypedDict):
    attentiveness_score: str
    customer_key: str
    duration: int
    failover: bool
    id: str
    join_time: str
    leave_time: str
    name: str
    status: str
    user_email: str
    user_id: str


@lru_cache()
def get_meeting_participant_events(token: str, meeting_id: int):
    """
    GET /report/meetings/{meetingId}/participants
    https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/reportMeetingParticipants
    """

    class MeetingParticipantReportResponse(TypedDict):
        page_count: int
        page_size: int
        total_records: int
        next_page_token: str
        participants: List[ParticipantReport]

    all_events = []
    next_page_token = ''
    while True:
        meeting_id_safe = urllib.parse.quote(urllib.parse.quote(meeting_id, safe=''), safe='')  # "Double encode" meeting uuid, needed if there's a forward slash
        url = f"https://api.zoom.us/v2/report/meetings/{meeting_id_safe}/participants?include_fields=registrant_id&page_size=300"
        if next_page_token:
            url += f'&next_page_token={next_page_token}'
        resp = requests.get(url, headers={"Authorization": f"Bearer {token}"})
        if not resp.ok:
            raise IOError(resp)

        data: MeetingParticipantReportResponse = resp.json()
        all_events.extend(data['participants'])
        if data['next_page_token']:
            next_page_token = data['next_page_token']
        else:
            return all_events

