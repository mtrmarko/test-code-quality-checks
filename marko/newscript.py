import requests
import datetime
import os

root = os.getcwd()
mydate = datetime.datetime.now()
print(f'In subfolder: {root} on this date and time: {mydate}')
response = requests.get('https://yahoo.com/')
print(response.content)
