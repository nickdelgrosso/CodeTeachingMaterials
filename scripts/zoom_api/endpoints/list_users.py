from __future__ import annotations

from functools import lru_cache
from typing import Literal, TypedDict, List

import requests


class User(TypedDict):
    id: str
    first_name: str
    last_name: str
    email: str
    type: int
    pim: int
    verified: int
    created_at: str
    group_ids: list[str]
    status: str
    role_id: str


def list_users(token: str, role_id: int = None):
    """
    https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/users
    """

    class UsersResponse(TypedDict):
        page_count: int
        page_number: int
        page_size: int
        total_records: int
        next_page_token: str
        users: List[User]

    params = {'role_id': role_id} if role_id is not None else None   

    resp = requests.get(
        f"https://api.zoom.us/v2/users",
        headers = {"Authorization": f"Bearer {token}"},
        params=params,
    )

    data: UsersResponse = resp.json()
    users = data["users"]
    return users
