import os
import requests

SERVICE_HOST = os.environ.get("SERVICE_HOST")
if not SERVICE_HOST:
    raise ValueError("SERVICE_HOST variable must be set")

class TestPokemon:
    """Tests for /pokemon/<name> route."""

    _session = requests.Session()

    def test_ok(self):
        response = self._session.get(f"http://{SERVICE_HOST}/pokemon/mewtwo")
        assert response.status_code == 200
        assert response.json() == {
            "description": "It was created by\na scientist after\nyears of horrific\fgene splicing and\nDNA engineering\nexperiments.",
            "habitat": "rare",
            "isLegendary": True,
            "name": "mewtwo"
        }
