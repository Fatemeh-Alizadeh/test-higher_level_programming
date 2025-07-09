#!/bin/bash
# Perform the request
[ "$(curl -s -w "%{http_code}" "$1")" = 200 ] && echo "$(curl -s "$1")"