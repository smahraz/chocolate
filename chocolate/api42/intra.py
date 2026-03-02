from .auth import ApiSession


URL_PREFIX = "https://api.intra.42.fr"


class IntraV2:
    @staticmethod
    def profile_info(login: str) -> dict:
        """
         /v2/users/:user_id
        """
        return ApiSession.get(URL_PREFIX + f"/v2/users/{login}")

    @staticmethod
    def validated_projects(
            campuses: list[str],
            markedat_from: str,
            markedat_to: str = "now",
            page_size: int = 100
    ) -> dict:
        """
        /v2/projects_users
        """

        params = {
            "range[marked_at]": f"{markedat_from},{markedat_to}",
            "page[size]": f"{page_size}"
        }

        if campuses:
            params.update({"filter[campus]": ",".join(campuses)})

        return ApiSession.get(
            URL_PREFIX + "/v2/projects_users",
            params=params
        )
