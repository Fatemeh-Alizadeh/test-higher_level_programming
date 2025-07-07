#!/bin/bash
# Send a request and get the size of the response body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"
