#!/usr/bin/python3

# lab 84 https://live.alta3.com/content/tlg-sde-python/labs/content/api/LAB_api_python_restful_api_requests_pokemon.html

import requests

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():
    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()

    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        # print(poke["name"])
        print(poke.get("name"))

    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")

if __name__ == "__main__":
    main()    