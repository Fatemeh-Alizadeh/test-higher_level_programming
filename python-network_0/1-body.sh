#!/bin/bash
# Perform the request
status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
[ "$status" -eq 200 ] && curl -s "$url"
