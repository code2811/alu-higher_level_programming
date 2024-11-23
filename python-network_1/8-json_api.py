#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter is sent in the variable q.
If no argument is given, q = ""
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    
    try:
        response = requests.post(url, data=data)
        json_response = response.json()
        
        if json_response:
            print("[{}] {}".format(
                json_response.get('id'),
                json_response.get('name')
            ))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")i
