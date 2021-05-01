#This file is used to find out how long it takes to connect to our apache server

import urllib.request
import time

#get start time
startTime = time.time()
ourPage = urllib.request.urlopen('https://google.com')
#success 
if (ourPage.getcode() == 200):
    print("Connected to the page successfully")
else: 
    print("Connection unsuccessful")
endTime = time.time()
elapsedTimeSeconds = endTime-startTime
elapsedTimeMilliSeconds = elapsedTimeSeconds*1000
print(elapsedTimeSeconds)
print(elapsedTimeMilliSeconds)
