Fetch status from https://alu-intranet.hbtn.io/status
    and display the response details
    """
    url = 'https://alu-intranet.hbtn.io/status'
    
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf8 content: {}".format(body.decode('utf-8')))
    
    except urllib.error.URLError as e:
        print("Error fetching status: {}".format(e))

if __name__ == "__main__":
    fetch_hbtn_status()
