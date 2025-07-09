#!/bin/bash
# Perform the request
[ "$(curl -s -o body.txt -w "%{http_code}" "$1")" -eq 200 ] && cat body.txt