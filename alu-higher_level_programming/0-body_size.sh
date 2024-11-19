#!/bin/bash
# A script to send a request to a URL and display the size of the body in bytes.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL and display the size of the body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"

