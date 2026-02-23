from .auth import ApiSession


URL_PREFIX = "https://api.intra.42.fr"


class IntraV2:
    @staticmethod
    def profile_info(login: str) -> dict:
        """
         /v2/users/:user_id
        """
        return ApiSession.get(URL_PREFIX + f"/v2/users/{login}")
