#!/usr/bin/env python3
"""DEMO: receiving JSON"""

# lab 90 https://live.alta3.com/content/tlg-sde-python/labs/content/api/LAB_api_jsonify.html

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app= Flask(__name__)

herodata= [{
    "name": "Spider-Man",
    "realName": "Peter Parker",
    "since": 1962,
    "powers": [
        "wall crawling",
        "web shooters",
        "spider senses",
        "super human strength & agility"
              ]
             }]

@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify(herodata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)