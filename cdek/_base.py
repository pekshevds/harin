from cdek.token import CDEKToken


def fetch_fake_client_id() -> str:
    """Открытые данные, предоставлены СДЭК"""
    return "wqGwiQx0gg8mLtiEKsUinjVSICCjtTEP"


def fetch_fake_client_secret() -> str:
    """Открытые данные, предоставлены СДЭК"""
    return "RmAmgvSgSl1yirlz9QupbzOJVqhCxcP5"


class CDEKBase:
    def __init__(self, token: CDEKToken, fake: bool = True):
        self.__token = token
        self.__fake = fake

    def _fetch_base_url(self) -> str:
        return "https://api.edu.cdek.ru" if self.__fake else "https://api.cdek.ru"

    def _fetch_base_header(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {str(self.__token)}",
            "content-type": "application/json",
        }
