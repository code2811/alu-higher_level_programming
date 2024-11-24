#!/usr/bin/python3
"""
Script that fetches https://alu-intranet.hbtn.io/status using urllib package
and displays the body response with specific formatting.
"""
import urllib.request


def fetch_status():
    """
    Fetches the status from ALU intranet and displays the response body
    with specific formatting for type, content, and utf8 content.
    """
    url = "https://alu-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()
