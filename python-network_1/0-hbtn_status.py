#!/usr/bin/python3
"""Module to fetch status from a given URL."""
import urllib.request

def fetch_status():
    """Fetch and display status from the specified URL."""
    url = 'https://intranet.hbtn.io/status'
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    except Exception as e:
        print("Error fetching status:", e)

if __name__ == "__main__":
    fetch_status()i
