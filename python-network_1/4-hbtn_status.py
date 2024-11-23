#!/usr/bin/python3
"""
Python script that fetches https://alu-intranet.hbtn.io/status
and displays the response body with specific formatting
"""
import requests


if __name__ == "__main__":
    r = requests.get("https://alu-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
