#!/bin/bash
# Script to retrieve body of response for a URL with 200 status code
curl -s -w "%{http_code}" "$1" | grep -qE "^200$" && curl -s "$1"i
