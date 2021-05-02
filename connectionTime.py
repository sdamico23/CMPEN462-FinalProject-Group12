#This file is used to find out how long it takes to connect to our apache server

import urllib.request
import time

#get start time
startTime = time.time()
ourPage = urllib.request.urlopen('http://192.168.31.237/')
#success 
if (ourPage.getcode() == 200):
    print("Connected to the page successfully")
else: 
    print("Connection unsuccessful")
endTime = time.time()
elapsedTimeSeconds = endTime-startTime
elapsedTimeMilliSeconds = elapsedTimeSeconds*1000
print("Time in seconds: " + str(elapsedTimeSeconds))
print("Time in milliseconds: " + str(elapsedTimeMilliSeconds))
