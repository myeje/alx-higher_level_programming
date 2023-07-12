#!/usr/bin/python3
"""Python function"""
import sys


save_to_json_file  = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

myFile = "add_item.json"

try:
    args = load_from_json_file(myFile)
except:
    args = []

args.extend(sys.argv[1:])
save_to_json_file(args, myFile)
