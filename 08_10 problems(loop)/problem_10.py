# exponential back off is concept in in each time you retry you face more dealy in execution.
# ex. when we are trying to login each time we retry for OTP we have to wait more and more time.

# Question : Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

waitTime=1
maxRetries=5
attempts=0

while attempts<maxRetries:
    print('attempts = ',attempts+1,' wait time = ',waitTime)
    time.sleep(waitTime)  # atla time mate system sleep


    waitTime*=2
    attempts+=1
