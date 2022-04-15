#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

# lab 83 https://live.alta3.com/content/tlg-sde-python/labs/content/api/LAB_api_python_restful_api_requests_game_of_thrones.html

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def name_finder(url_list):
    names = []
    for url in url_list:
        name = requests.get(url).json().get("name")
        names.append(name)
    return names


def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        # pprint.pprint(got_dj)

        print()

        print("This character has allegiances to:")
        for house in name_finder(got_dj.get("allegiances")):
            print(house)

        print()    
        
        print("This character appears in these books:")
        for book in name_finder(got_dj.get("books")):
            print(book)

if __name__ == "__main__":
        main()
