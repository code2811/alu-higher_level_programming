#!/bin/bash
# Script to retrieve the size of the body response from a given URL
curl -sI "$1" | grep -i "Content-Length:" | awk '{print $2}'
