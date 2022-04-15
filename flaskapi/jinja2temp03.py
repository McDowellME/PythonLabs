#!/usr/bin/python3

# lab 92 https://live.alta3.com/content/tlg-sde-python/labs/content/api/LAB_api_python_flask_jinja.html


from flask import Flask
from flask import render_template

app = Flask(__name__)

# pull in the value of score as an int
@app.route("/scoretest/<int:score>")
def hello_name(score):
    # render the template with the value of score for marks
    # marks is a jinja var in the template
    return render_template("highscore.html", marks = score)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)