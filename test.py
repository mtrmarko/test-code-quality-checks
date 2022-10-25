import requests
import datetime
import os

root = os.getcwd()
mydate = datetime.datetime.now()
print(f'In folder: {root} on this date and time: {mydate}')
response = requests.get('https://google.com/')
print(response.content)
