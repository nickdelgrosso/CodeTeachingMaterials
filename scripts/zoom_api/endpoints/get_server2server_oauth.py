from __future__ import annotations

from base64 import b64encode
from typing import TypedDict, NewType

import requests

AccessToken = NewType("AccessToken", str)

class OAuth(TypedDict):
    access_token: AccessToken
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
    if response.ok:
        oauth: OAuth = response.json()
        return oauth
    else:
        raise IOError
