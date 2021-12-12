import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout
from requests.sessions import TooManyRedirects


class ProviderException(Exception):
    """Base exception for all providers."""


class NetworkError(ProviderException):
    """Generic networking error happened when communicating with the API."""


class ApplicationError(ProviderException):
    """Third-party API returned application error."""


class APIClient:
    """
    Simple class to do API calls to third-party APIs.

    Incapsulates base errors handling and response parsing.
    """

    def __init__(self, base_url: str):
        self.session = requests.Session()
        self.base_url = base_url.strip("/")

    def _request(self, method: str, url: str, **kwargs):
        kwargs.setdefault("timeout", 10)
        url = f"{self.base_url}{url}"

        try:
            response = getattr(self.session, method)(url, **kwargs)
        except (ConnectionError, Timeout, TooManyRedirects):
            raise NetworkError()  # may consider retry the request

        try:
            response.raise_for_status()
        except HTTPError:
            raise ApplicationError()  # 400s and 500s

        return response.json()

    def get(self, url: str):
        return self._request("get", url)

    def post(self, url: str, payload: dict):
        return self._request("post", url, json=payload)
