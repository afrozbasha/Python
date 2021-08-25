"""
    @Author: Afroz Basha
    @Date: 2021-08-25
    @Title: 2D ARRAY
"""
import time

"""
Description:
    Write a Stopwatch Program for measuring the time that elapses between the start and end clicks
Parameter:
    Using Try and except
Return:
   It turns total Seconds taken in Stop watch
"""

try:
    while True:
        start = input("Type to `start` to Start the Stopwatch : ")
        statTime = time.time()
        stop = input("Type to `stop` to Start the Stopwatch : ")
        stopTime = time.time()
        timeElapsed = stopTime - statTime
        print("Time elapsed from Starting time to Stopping time is: ", timeElapsed)
except ValueError:
    print("Enter `start` and `stop` only")