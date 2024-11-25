#!/usr/bin/python3
"""
Module to fetch and display status from a given URL.

This script demonstrates how to use urllib to fetch
a status page and display its contents with detailed information.
"""
import urllib.request

def fetch_status(url):
    """
    Fetch status from the specified URL and display response details.

    Args:
        url (str): The URL to fetch status from.

    Returns:
        None
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    
    except urllib.error.URLError as e:
        print("Error fetching status: {}".format(e))

def main():
    """
    Main function to demonstrate URL status fetching.
    
    Fetches status from multiple possible URLs.
    """
    urls = [
        'https://intranet.hbtn.io/status',
        'http://0.0.0.0:5050/status'
    ]
    
    for url in urls:
        fetch_status(url)
