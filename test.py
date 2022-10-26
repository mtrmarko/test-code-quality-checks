import datetime
import os
import requests
import sqlite3

root = os.getcwd()
mydate = datetime.datetime.now()
print(f'In folder: {root} on this date and time: {mydate} hhhhhhhhhhhhhhhhhhhgjhghhhhhhhhhhhhhhbhhhmhjhkjdfdf')
response = requests.get("https://google.com/")
print(response.content)
