#!/usr/bin/python3
"""
Module to fetch status from a given URL using urllib.
Displays response details as specified.
"""
import urllib.request

def fetch_status():
    """
    Fetch and display status from the specified URL.
    """
    url = 'https://intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))

if __name__ == "__main__":
    fetch_status()i
