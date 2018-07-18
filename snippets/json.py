"""
Simple python script to query user details and save them to a text file
"""

from json import dumps, load
import os


with open('data.json') as f:
    data = load(f)

print(data)
