from __future__ import annotations

import os
from typing import Any

import pytest
import requests

SERVICE_HOST = os.environ.get("SERVICE_HOST")
if not SERVICE_HOST:
    raise ValueError("SERVICE_HOST variable must be set")

KNOWN_POKEMONS = {
    "mewtwo": {
        "description": "It was created by\na scientist after\nyears of horrific\fgene splicing and\nDNA engineering\nexperiments.",
        "habitat": "rare",
        "isLegendary": True,
        "name": "mewtwo",
    },
    "wormadam": {
        "description": "When BURMY evolved, its cloak\nbecame a part of this Pokémon’s\nbody. The cloak is never shed.",
        "habitat": "",
        "isLegendary": False,
        "name": "wormadam",
    },
}

EXPECTED_TRANSLATIONS = {
    "mewtwo": "Created by a scientist after years of horrific gene splicing and dna engineering experiments,  it was.",
    "wormadam": "At which hour burmy evolved,  its cloak did doth becometh a part of this pokémon’s corse. The cloak is nev'r did shed.",
}


class TestPokemon:
    """Tests for /pokemon/<name> route."""

    _session = requests.Session()

    @pytest.mark.parametrize(["name", "expected_result"], KNOWN_POKEMONS.items())
    def test_ok(self, name: str, expected_result: dict[str, Any]):
        response = self._session.get(f"http://{SERVICE_HOST}/pokemon/{name}")
        assert response.status_code == 200
        assert response.json() == expected_result


class TestTranslatedPokemon:
    """Tests for /pokemon/translated/<name> route."""

    _session = requests.Session()

    @pytest.mark.parametrize(
        ["name", "expected_result"],
        [
            (name, dict(response, description=EXPECTED_TRANSLATIONS[name]))
            for name, response in KNOWN_POKEMONS.items()
        ],
    )
    def test_ok(self, name: str, expected_result: dict[str, Any]):
        response = self._session.get(f"http://{SERVICE_HOST}/pokemon/translated/{name}")
        assert response.status_code == 200
        assert response.json() == expected_result
