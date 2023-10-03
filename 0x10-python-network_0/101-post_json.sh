#!/bin/bash
#Bash script sends a JSON request to URL passed as arg and display body of response
curl -s -H "Content-Type: application/json" -d @"$2" -X POST "$1"
