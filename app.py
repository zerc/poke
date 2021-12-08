from __future__ import annotations

from flask import Flask, jsonify

from providers import pokeapi

app = Flask(__name__)


@app.route("/pokemon/<name>")
def get_pokemon(name: str):
    return jsonify(pokeapi.get_pokemon(name))
