#!/usr/bin/env python3
"""Basic Flask app with a single GET route."""
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/', methods=['GET'])
def welcome():
    """
    GET route that returns a JSON payload.
    """
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    