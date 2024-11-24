#!/usr/bin/python3
"""Script that takes URL and email as input, sends POST request, displays response"""
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    Send POST request to URL with email parameter and print response
    Args:
        url: target URL to send POST request
        email: email to be sent as parameter
    """
    # Prepare the email data to be sent
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    try:
        # Create request object with URL and data
        req = urllib.request.Request(url, data=data, method='POST')

        # Send request and get response using with statement
        with urllib.request.urlopen(req) as response:
            # Read and decode response
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.URLError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Get URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
