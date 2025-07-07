#!/bin/bash
# Perform the request
response=$(curl -s -w "\n%{http_code}" "$1")

# Split body and status code
body=$(echo "$response" | sed '$d')
status=$(echo "$response" | tail -n 1)

# Display body only if status is 200
if [ "$status" -eq 200 ]; then
  echo "$body"
fi