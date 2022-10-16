from __future__ import annotations

from typing import TypedDict, List

import requests


class Role(TypedDict):
    id: str
    name: str
    description: str
    total_members: int


def list_roles(token: str) -> List[Role]:

    class RolesResponse(TypedDict):
        total_records: int
        roles: List[Role]

    resp = requests.get(
        f"https://api.zoom.us/v2/roles",
        headers = {"Authorization": f"Bearer {token}"},
    )
    data: RolesResponse = resp.json()

    roles = data["roles"]
    return roles
