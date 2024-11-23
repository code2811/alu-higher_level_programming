import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # GitHub API endpoint for user information
    url = "https://api.github.com/user"

    # Create Basic Authentication header using username and token
    response = requests.get(url, auth=(username, token))

    # Check if authentication was successful and print user ID
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)i
