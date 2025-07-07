#!/bin/bash
# Perform the request
response=$(curl -s -w "\n%{http_code}" "$1")
[ "$(echo "$response" | tail -n1)" = "200" ] && echo "$response" | sed '$d'