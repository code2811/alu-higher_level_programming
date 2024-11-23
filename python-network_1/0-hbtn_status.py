#!/usr/bin/python3
"""A Python script that fetches a status URL.

This script uses urllib package to make a request to a URL
and displays information about the response including its
type, content in bytes, and UTF-8 decoded content.
"""
from urllib import request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))i
