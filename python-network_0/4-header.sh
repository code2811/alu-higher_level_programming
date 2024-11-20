#!/bin/bash
# Script that sends a GET request with X-HolbertonSchool-User-Id header
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
