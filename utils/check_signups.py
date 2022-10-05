from __future__ import annotations

import os
from base64 import b64encode
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, TypedDict
from warnings import warn

import requests

## Logging In

@dataclass(frozen=True)
class Credentials:
    zoom_account_id: str
    zoom_client_id: str
    zoom_client_secret: str

    @classmethod
    def from_environment_variables(
        cls, 
        zoom_account_id="ZOOM_ACCOUNT_ID",
        zoom_client_id="ZOOM_CLIENT_ID", 
        zoom_client_secret="ZOOM_CLIENT_SECRET",
    ) -> Credentials:
        return cls(
            zoom_account_id=os.getenv(key=zoom_account_id),
            zoom_client_id=os.getenv(key=zoom_client_id),
            zoom_client_secret=os.getenv(key=zoom_client_secret),
        )



class OAuth(TypedDict):
    access_token: str
    token_type: str
    expires_in: int
    scope: str


def get_server2server_oauth(account_id: str, client_id: str, client_secret: str) -> OAuth:
    """
    Get access for server2server docs.
    Based on example from https://marketplace.zoom.us/docs/guides/build/server-to-server-oauth-app/#use-account-credentials-to-get-an-access-token
    curl -X POST -H 'Authorization: Basic Base64Encoder(clientId:clientSecret)' https://zoom.us/oauth/token?grant_type=account_credentials&account_id={accountId}

    """
    auth_code = b64encode(f"{client_id}:{client_secret}".encode()).decode()
    response = requests.post(
        url=f"https://zoom.us/oauth/token?grant_type=account_credentials&account_id={account_id}",
        headers={
            'Authorization': f"Basic {auth_code}",
        }
    )
    oauth: OAuth = response.json()
    return oauth



## API: List Meetings


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

def list_meetings(token: str, user_id="me", page_size: int = 100) -> List[Meeting]:


    class MeetingResponse(TypedDict):
        page_size: int
        total_records: int
        next_page_token: Optional[str]
        meetings: List[Meeting]

    resp = requests.get(
        f"https://api.zoom.us/v2/users/{user_id}/meetings?page_size={page_size}",
        headers = {"Authorization": f"Bearer {token}"}
    )

    data: MeetingResponse = resp.json()
    if data['page_size'] < data['total_records']:
        warn(f"Only extracting {data['page_size']} of {data['total_records']} meetings")

    meetings = data["meetings"]
    return meetings


## API: List Meeting Registrants

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


## API: List Roles

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
    

## API: List Users

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


def list_users(token: str):

    class UsersResponse(TypedDict):
        page_count: int
        page_number: int
        page_size: int
        total_records: int
        next_page_token: str
        users: List[User]

    resp = requests.get(
        f"https://api.zoom.us/v2/users",
        headers = {"Authorization": f"Bearer {token}"},
    )

    data: UsersResponse = resp.json()
    users = data["users"]
    return users

#####################

if __name__ == '__main__':

    # Get Credentials
    creds = Credentials.from_environment_variables()
    oauth = get_server2server_oauth(
        account_id=creds.zoom_account_id, 
        client_id=creds.zoom_client_id, 
        client_secret=creds.zoom_client_secret,
    )
    token = oauth["access_token"]


    # Get all the User Roles
    roles = list_roles(token=token)    
    print(f'--------- Account Roles----------------')
    for role in roles:
        print(f"{role['id']}  {role['name']} ({role['total_members']} Users): {role['description']}")


    # Get the Users
    users = list_users(token=token)
    print(f'----------Users---------------')
    for user in sorted(users, key=lambda d: (d['role_id'], d["last_name"], d["first_name"])):
        print(f"{user['id']} (Role {user['role_id']}):  {user['last_name']}, {user['first_name']}:  {user['email']}")


    # Get the Admin's Meetings
    for user in users:
        if user["role_id"] == "0":  # if user is an admin...
            admin = user
            break
    else:
        raise ValueError("Admin not found.")


    meetings = list_meetings(token=token, user_id=admin["id"])
    print('------------Meetings--------------')
    for meeting in sorted(meetings, key=lambda d: d["start_time"], reverse=True):
        print(f"{meeting['id']}: {meeting['start_time']}  {meeting['topic']}  {meeting['join_url']}")
    

    # Get the registrants from a requested Meeting
    meeting_id = 86860544676
    registrants = list_registrants(token=token, meeting_id=meeting_id)
    print(f'-------{len(registrants)} Registrants for Meeting {meeting_id}------------')
    for registrant in sorted(registrants, key=lambda d: (d["last_name"], d["first_name"])):
        print(f"{registrant['last_name']}, {registrant['first_name']}")