#!/bin/bash
# Script to send GET request with custom header and validate route
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1" -w "%{http_code}"
