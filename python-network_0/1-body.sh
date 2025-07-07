#!/bin/bash
# Perform the request
[ "$(curl -s -o /dev/null -w "%{http_code}" "$url")" -eq 200 ] && curl -s "$url"

