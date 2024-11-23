i
n script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    # Set default value for q if no argument is provided
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send POST request with q parameter
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}
    response = requests.post(url, data=data)

    try:
        # Try to parse JSON response
        json_response = response.json()
        
        # Check if response is empty
        if json_response:
            print("[{}] {}".format(
                json_response.get('id'),
                json_response.get('name')
            ))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
