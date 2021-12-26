from __future__ import annotations
from os import environ

from dataclasses import dataclass
from functools import lru_cache

from providers.base import APIClient

base_url = environ.get("POKEAPI_BASE_URL", "https://pokeapi.co/api/v2")
client = APIClient(base_url)

@dataclass
class Pokemon:
    name: str
    description: str
    habitat: str
    isLegendary: bool


def get_pokemon(name: str) -> Pokemon:
    data = _request(name)
    return Pokemon(
        name=data["name"],
        description=data["description"],
        habitat=data["habitat"],
        isLegendary=(data["is_legendary"] == "True"),
    )


@lru_cache(maxsize=512)
def _request(name: str) -> dict[str, str]:
    """Returns a subset of raw data."""
    raw_data = client.get(f"/pokemon-species/{name}/")
    habitat = raw_data["habitat"]["name"] if raw_data["habitat"] else ""
    return {
        "name": raw_data["name"],
        "description": raw_data["flavor_text_entries"][0]["flavor_text"],
        "habitat": habitat,
        "is_legendary": ["False", "True"][
            raw_data["is_legendary"]
        ],  # HACK: to make mypy happy
    }
