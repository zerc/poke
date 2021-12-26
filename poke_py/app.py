from __future__ import annotations

from os import environ

from flask import Flask, jsonify, url_for
from providers import funtransapi, pokeapi

app = Flask(__name__)


@app.route("/pokemon/<name>")
def get_pokemon(name: str):
    return jsonify(pokeapi.get_pokemon(name))


@app.route("/pokemon/translated/<name>")
def get_pokemon_translated(name: str):
    pokemon = pokeapi.get_pokemon(name)

    if pokemon.habitat == "cave" or pokemon.isLegendary:
        pokemon.description = funtransapi.as_yoda(pokemon.description)
    else:
        pokemon.description = funtransapi.as_shakespeare(pokemon.description)

    return jsonify(pokemon)


@app.route("/")
def index():
    return jsonify(
        {
            "pokemon": url_for("get_pokemon", name="mewtwo"),
            "pokemon_translated": url_for("get_pokemon_translated", name="mewtwo"),
        }
    )


if __name__ == "__main__":
    host = environ.get("SERVER_HOST", "127.0.0.1")
    port = int(environ.get("SERVER_PORT", 8080))
    app.run(host=host, port=port)
