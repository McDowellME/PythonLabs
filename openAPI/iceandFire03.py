#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

# lab 83 https://live.alta3.com/content/tlg-sde-python/labs/content/api/LAB_api_python_restful_api_requests_game_of_thrones.html

import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send HTTPS GET to the API of ICE and Fire books resource
    gotresp = requests.get(AOIF_BOOKS)

    ## Decode the response
    got_dj = gotresp.json()

    ## loop across response
    for singlebook in got_dj:
        ## display the names of each book
        ## all of the below statements do the same thing
        #print(singlebook["name"] + ",", "pages -", singlebook["numberOfPages"])
        #print("{}, pages - {}".format(singlebook["name"], singlebook["numberOfPages"]))
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")
        # print ISBN
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")

if __name__ == "__main__":
    main()