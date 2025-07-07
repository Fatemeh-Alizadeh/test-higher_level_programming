#!/bin/bash
status=$(curl -s -w "\n%{http_code}" "$1" | tee /tmp/body | tail -n1)
[ "$status" = "200" ] && sed '$d' /tmp/body