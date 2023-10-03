#!/bin/bash
# bash script takes a URL as arg, sends GET request and displays body of response
curl -sX GET -H "X-School-User-Id:98" "$1"
