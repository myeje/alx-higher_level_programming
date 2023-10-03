#!/bin/bash
# Bash script takes in a URL, sends a request to it and displays the size
curl -s "$1" | wc -c
