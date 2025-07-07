#!/bin/bash
# Check if a URL was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi
# Send a request and get the size of the response body in bytes
curl -s -o /dev/null -w "%{size_download}\n" "$1"
