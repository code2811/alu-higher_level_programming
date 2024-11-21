#!/bin/bash
# Script to send a GET request with a custom header and validate response

# Check if URL is provided
if [ $# -eq 0 ]; then
    echo "Please provide a URL"
    exit 1
fi

# Send GET request with the specified custom header and capture response
response=$(curl -s -H "X-HolbertonSchool-User-Id: 98" "$1")

# Echo the response
echo "$response"
