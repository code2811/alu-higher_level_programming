#!/bin/bash
# Displays the size of the body of the response from a given URL in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"

