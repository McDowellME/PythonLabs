#!/usr/bin/env python3

# lab 90 https://live.alta3.com/content/tlg-sde-python/labs/content/api/LAB_api_jsonify.html

import requests
from pprint import pprint

URL= "http://127.0.0.1:2224/"

resp= requests.get(URL).json()

pprint(resp)