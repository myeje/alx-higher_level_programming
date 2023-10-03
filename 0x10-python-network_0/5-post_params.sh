#!/bin/bash
# Bash script takes URL, sends POST request and displays body of the response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
