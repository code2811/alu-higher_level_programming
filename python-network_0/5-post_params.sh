#!/bin/bash
# Script that sends a POST request with email and subject parameters
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"i
