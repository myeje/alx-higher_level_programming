#!/bin/bash
# Bash script sends a request to URL passed as arg and displays status code
curl -s -o /dev/null -w "%{http_code}" "$1"
