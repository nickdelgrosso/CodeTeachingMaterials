from __future__ import annotations

import os
from dataclasses import dataclass

from zoom_api.endpoints.get_server2server_oauth import OAuth, get_server2server_oauth


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
        zoom_account_id_value = os.getenv(key=zoom_account_id)
        if not zoom_account_id_value:
            raise OSError(f"No value found for {zoom_account_id}")

        zoom_client_id_value = os.getenv(key=zoom_client_id)
        if not zoom_client_id_value:
            raise OSError(f"No value found for {zoom_client_id}")

        zoom_client_secret_value = os.getenv(key=zoom_client_secret)
        if not zoom_client_secret_value:
            raise OSError(f"No value found for {zoom_client_secret}")

        return cls(
            zoom_account_id=zoom_account_id_value,
            zoom_client_id=zoom_client_id_value,
            zoom_client_secret=zoom_client_secret_value,
        )

    def get_oauth(self) -> OAuth:
        return get_server2server_oauth(
            account_id=self.zoom_account_id,
            client_id=self.zoom_client_id,
            client_secret=self.zoom_client_secret,
        )

