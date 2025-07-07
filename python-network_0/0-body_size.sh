#!/bin/bas
# Send a request and get the size of the response body in bytes
curl -s -o -w "%{size_download}\n" "$1"
