import datetime
import os

import requests
import sqlite3

root = os.getcwd()
mydate = datetime.datetime.now()
print(f"In subfolder: {root} on this date and time: {mydate} blllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
response = requests.get("https://yahoo.com/")
print(response.content)
