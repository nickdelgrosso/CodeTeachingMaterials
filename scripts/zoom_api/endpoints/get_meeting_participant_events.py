from __future__ import annotations

from typing import TypedDict, List

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

    resp = requests.get(
        f"https://api.zoom.us/v2/report/meetings/{meeting_id}/participants?include_fields=registrant_id&page_size=300",
        # f"https://api.zoom.us/v2/report/meetings/{meeting_id}",
        headers = {"Authorization": f"Bearer {token}"},
    )
    assert resp.content
    data: MeetingParticipantReportResponse = resp.json()

    participants = data['participants']
    return participants
