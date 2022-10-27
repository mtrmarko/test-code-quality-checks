"""This is some test module of mine
Blah blah blah blah
Ha, maybe it's fixed now
"""
import datetime
import os

import requests

root = os.getcwd()
mydate = datetime.datetime.now()
print(f"In folder: {root} on this date and time: {mydate}")
response = requests.get("https://google.com/")
print(response.content)
