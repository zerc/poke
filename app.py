from __future__ import annotations

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/pokemon/<name>")
def get_pokemon(name: str):
    return jsonify(
        {
            "name": name,
            "description": (
                "It was created by a scientist after years of horrific genesplicing and DNA engineering experiments."
            ),
            "habitat": "rare",
            "isLegendary": True,
        }
    )
