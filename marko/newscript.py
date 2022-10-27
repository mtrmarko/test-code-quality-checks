import datetime
import os
import sqlite3
import requests

root = os.getcwd()
mydate = datetime.datetime.now()
print(f"In subfolder: {root} on this date and time: {mydate} blllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
response = requests.get("https://yahoo.com/")
print(response.content)
