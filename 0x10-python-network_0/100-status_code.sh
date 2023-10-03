#!/bin/bash
# Bash script sends a request to URL passed as arg and displays status code
curls -s -o /dev/null -w "%{http_code}" "$1"
