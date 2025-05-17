from dataclasses import dataclass, asdict
from datetime import datetime
from httpx import Client, codes


@dataclass(frozen=True, kw_only=True)
class CDEKAuth:
    grant_type: str = "client_credentials"
    client_id: str
    client_secret: str


class CDEKToken:
    def __init__(self, cdek_auth: CDEKAuth, fake: bool = True) -> None:
        self.__cdek_auth = cdek_auth
        self.__fake = fake
        self.__token = ""
        self.update_token()

    def update_token(self) -> None:
        self.__update_date = datetime.now()
        self.__token = self._fetch_token()

    def need_update_token(self) -> bool:
        live_time = 3600
        return (datetime.now() - self.__update_date).total_seconds() > live_time

    def ok(self) -> bool:
        return self.__token == ""

    def _fetch_token(self) -> str:
        responce = Client().post(
            url=("https://api.edu.cdek.ru" if self.__fake else "https://api.cdek.ru")
            + "/v2/oauth/token",
            headers={"content-type": "application/x-www-form-urlencoded"},
            params=asdict(self.__cdek_auth),
        )
        if responce.status_code != codes.OK:
            return ""
        return responce.json().get("access_token", "")

    def __str__(self) -> str:
        return self.__token
