from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from providers.base import APIClient

client = APIClient("https://pokeapi.co/api/v2")


@dataclass
class Pokemon:
    name: str
    description: str
    habitat: str
    isLegendary: bool


@lru_cache(maxsize=512)
def get_pokemon(name: str) -> Pokemon:
    raw_data = client.get(f"/pokemon-species/{name}/")
    habitat = raw_data["habitat"]

    return Pokemon(
        name=raw_data["name"],
        description=raw_data["flavor_text_entries"][0]["flavor_text"],
        habitat=habitat["name"] if habitat else "",
        isLegendary=raw_data["is_legendary"],
    )
