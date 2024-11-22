#!/usr/bin/python3
"""Module to retrieve X-Request-Id from URL response header."""
import urllib.request
import sys

def get_x_request_id(url):
    """
    Send request to URL and print X-Request-Id header value.
    
    Args:
        url (str): URL to send request to
    """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)

if __name__ == "__main__":
    get_x_request_id(sys.argv[1])ii
