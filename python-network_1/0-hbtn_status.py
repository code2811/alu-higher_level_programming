#!/usr/bin/python3
"""
Module to fetch and display status from a given URL.

This script uses urllib to retrieve the status of a specified URL
and prints details about the response body.
"""
import urllib.request

def fetch_status(url='https://intranet.hbtn.io/status'):
    """
    Fetch status from the given URL and display response details.

    Args:
        url (str): URL to fetch status from. 
                   Defaults to 'https://intranet.hbtn.io/status'
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()
        
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))

if __name__ == "__main__":
    fetch_status()i
