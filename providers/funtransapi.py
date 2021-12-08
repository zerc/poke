import requests

session = requests.Session()
BASE_URL = "https://api.funtranslations.com/translate"


def as_yoda(text: str) -> str:
    return _do_request("yoda", text)


def as_shakespeare(text: str) -> str:
    return _do_request("shakespeare", text)


def _do_request(translation_name: str, text: str) -> str:
    response = session.post(f"{BASE_URL}/{translation_name}.json", json={"text": text})
    response.raise_for_status()
    data = response.json()
    return data["contents"]["translated"]
