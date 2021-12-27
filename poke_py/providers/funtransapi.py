from __future__ import annotations

from os import environ

from providers.base import APIClient

base_url = environ.get("FUNTRANS_BASE_URL", "https://api.funtranslations.com/translate")
client = APIClient(base_url)


def as_yoda(text: str) -> str:
    return _do_request("yoda", text)


def as_shakespeare(text: str) -> str:
    return _do_request("shakespeare", text)


def _do_request(translation_name: str, text: str) -> str:
    data = client.post(f"/{translation_name}.json", payload={"text": text})
    return data["contents"]["translated"]
