#!/usr/bin/python3
"""
Python script that fetches http://0.0.0.0:5050/status
and displays the response body with specific formatting
"""
import requests


if __name__ == "__main__":
    r = requests.get("http://0.0.0.0:5050/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
