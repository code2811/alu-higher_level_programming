#!/bin/bash
# Script to send GET request with custom X-HolbertonSchool-User-Id header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
