"""This is another test module of mine
Blah blah blah blah
Ha, maybe it's fixed now
"""
import datetime
import os

import requests

root = os.getcwd()
mydate = datetime.datetime.now()
print(f"In subfolder: {root} on this date and time: {mydate} ")
response = requests.get("https://yahoo.com/")
print(response.content)
