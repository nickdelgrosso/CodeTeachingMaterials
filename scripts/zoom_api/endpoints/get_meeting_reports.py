from __future__ import annotations

from typing import Iterable, Tuple, TypedDict, List
from warnings import warn
import requests
from dateutil.parser import parse as parse_date
from datetime import datetime, timedelta

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


def get_meeting_reports(token: str, user_id, from_: str, to: str, type='past') -> List[Meeting2]:
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
    
    assert resp.ok, resp.text
    assert resp.content

    data: ReportUserMeetingsResponse = resp.json()

    # Validate response matches request
    if data['from'] != from_ or data['to'] != to:
        warn(f"Requested dates {from_}-{to}, received {data['from']}-{data['to']}.")

    return data['meetings']



def get_all_meeting_reports(token: str, user_id, from_: str, to: str, type='past') -> List[Meeting2]:
    """Calls get_meeting_reports repeatedly for each month's worth of data, and gathers it up."""
    orig_from = parse_date(from_)
    orig_to = parse_date(to)

    if orig_to > (orig_from + timedelta(days=183)):
        warn(f'Requesting more than zoom\'s stored 6 months requested between {from_} and {to}.')

    
    all_meetings = []
    for start, stop in date_range(parse_date(from_), parse_date(to), timedelta(days=30), spacing=timedelta(days=1)):
        print(start, stop)
        meetings = get_meeting_reports(
            token=token,
            user_id=user_id,
            from_=start.strftime('%Y-%m-%d'),
            to=stop.strftime('%Y-%m-%d'),
        )
        all_meetings.extend(meetings)

    return all_meetings
    

def date_range(start: datetime, stop: datetime, step: timedelta, spacing: timedelta = timedelta()) -> Iterable[Tuple[datetime, datetime]]:
    """
    Yields pairs of dates, ending with the stop date, with rought "step" sizes.  Can add non-overlapping spacing.

    Note: atm, this function doesn't try to get equal-size steps.
    """
    if start > stop:
        raise ValueError("start date must be earlier than stop date.")

    t1 = start 
    while t1 < stop:
        t0 = t1
        t1 += step
        if t1 > stop:
            t1 = stop
        yield t0, t1
        t1 += spacing
    

