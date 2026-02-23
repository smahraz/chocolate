from typing import Any, Callable
from datetime import datetime
from os import getenv
from dotenv import load_dotenv
import functools
import requests


load_dotenv()
API_UID = getenv("API_UID")
API_SECRET = getenv("API_SECRET")


assert API_UID is not None, "API_UID is missing from `.env` file"
assert API_SECRET is not None, "API_SECRET is missing from `.env` file"


class ApiSession:
    token: str = ""
    token_type: str
    token_life_in_second: int
    token_creation_date: datetime

    @staticmethod
    def _validate_before_requests(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(cls, *args, **kwargs):
            if not cls.token or cls._is_token_expired():
                cls.auth()
            headers = {
                "Authorization": f"{cls.token_type} {cls.token}"
            }
            kwargs.update(headers=headers)
            return func(cls, *args, **kwargs)
        return wrapper

    @classmethod
    @_validate_before_requests
    def get(cls, *args, **kwargs) -> dict[str, Any]:
        return requests.get(*args, **kwargs).json()

    @classmethod
    def auth(cls) -> None:
        resp = cls._get_oauth_token()

        cls.token = resp["access_token"]
        cls.token_type = resp["token_type"]
        cls.token_life_in_second = resp["expires_in"]
        cls.token_creation_date = datetime.now()

    @classmethod
    def _is_token_expired(cls) -> bool:
        lived = datetime.now() - cls.token_creation_date
        return cls.token_life_in_second <= lived.seconds

    @staticmethod
    def _get_oauth_token() -> dict[str, Any]:
        url = "https://api.intra.42.fr/oauth/token"
        data = {
            "grant_type": "client_credentials",
            "client_id": API_UID,
            "client_secret": API_SECRET
        }
        r = requests.post(url, data=data)

        return r.json()


if __name__ == "__main__":

    print(ApiSession.get("https://api.intra.42.fr/oauth/token/info"))
    print(ApiSession.get("https://api.intra.42.fr/oauth/token/info"))
