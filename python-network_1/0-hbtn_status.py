#!/usr/bin/python3
"""
A script that fetches the content of a given URL using urllib.

The body of the response is displayed with:
    - type: the type of the response content
    - content: the raw content (bytes)
    - utf8 content: the decoded content (string)
"""

import urllib.request

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"  # You can replace this with any URL.

    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
i
