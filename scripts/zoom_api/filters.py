
from enum import Enum
from typing import TypedDict


class Meeting(TypedDict):
    type: int


class MeetingType(Enum):
    """
    Meeting Type(s)
    Reference: Response section of https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/reportMeetings

    1 — An instant meeting.
    2 — A scheduled meeting.
    3 — A recurring meeting with no fixed time.
    4 — A personal meeting room.
    8 — A recurring meeting with a fixed time.
    """
    Instant = 1
    Scheduled = 2
    RecurringNoFixedTime = 3
    PersonalMeetingRoom = 4
    RecurringFixedTime = 8


def meeting_type_is(meeting: Meeting, *meeting_types: MeetingType) -> bool:
    """Return whether the meeting is of a particular type."""
    return meeting['type'] in [meeting_type.value for meeting_type in meeting_types]
        