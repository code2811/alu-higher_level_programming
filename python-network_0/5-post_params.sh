#!/bin/bash
# Script to send POST request with email and subject parameters
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"i
