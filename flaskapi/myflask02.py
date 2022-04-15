#!/usr/bin/python3

# lab 89 https://live.alta3.com/content/tlg-sde-python/labs/content/api/LAB_api_python_flask_builing_apis.html

from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"
    ## V2 STYLE STRING FORMATTER - return "Hello {}".format(name)
    ## OLD STYLE STRING FORMATTER - return "Hello %s!" % name

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application