from __future__ import annotations

from typing import TypedDict, List

import requests


class Registrant(TypedDict):
    address: str
    city: str
    comments: str
    country: str
    create_time: str
    custom_questions: List
    email: str
    first_name: str
    id: str
    industry: str
    job_title: str
    join_url: str
    last_name: str
    no_of_employees: str
    org: str
    phone: str
    purchasing_time_frame: str
    role_in_purchase_process: str
    state: str
    status: str  # approved, denied, or pending
    zip: str


def list_registrants(token: str, meeting_id: int) -> List[Registrant]:
    class RegistrantsResponse(TypedDict):
        page_size: int
        total_records: int
        next_page_token: str
        registrants: list[Registrant]

    resp = requests.get(
        f"https://api.zoom.us/v2/meetings/{meeting_id}/registrants",
        headers = {"Authorization": f"Bearer {token}"},
    )
    data: RegistrantsResponse = resp.json()
    registrants = data['registrants']
    return registrants
