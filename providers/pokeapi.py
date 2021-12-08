from __future__ import annotations

from dataclasses import dataclass

import requests

BASE_URL = "https://pokeapi.co/api/v2"

session = requests.Session()


@dataclass
class Pokemon:
    name: str
    description: str
    habitat: str
    isLegendary: bool


def get_pokemon(name: str) -> Pokemon:
    response = session.get(f"{BASE_URL}/pokemon-species/{name}/", timeout=10)
    response.raise_for_status()

    raw_data = response.json()
    habitat = raw_data["habitat"]

    return Pokemon(
        name=raw_data["name"],
        description=raw_data["flavor_text_entries"][0]["flavor_text"],
        habitat=habitat["name"] if habitat else "",
        isLegendary=raw_data["is_legendary"],
    )
