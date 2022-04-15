#!/usr/bin/env python3

# lab 92 https://live.alta3.com/content/tlg-sde-python/labs/content/api/LAB_api_python_flask_jinja.html

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hellobasic.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)