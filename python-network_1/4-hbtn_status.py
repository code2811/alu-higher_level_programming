#!/usr/bin/python3
"""
Script that fetches https://alu-intranet.hbtn.io/status using requests package
and displays the body response with specific formatting.
"""
import requests


def fetch_status():
    """
    Fetches the status from ALU intranet and displays the response body
    with specific formatting for type and content.
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch_status()
