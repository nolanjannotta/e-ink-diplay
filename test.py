
import os

import schedule
import time

def hello():
    print("hello")

schedule.every(1).minutes.do(hello)

while True:
    schedule.run_pending()
    time.sleep(1)



#picdir = (os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')

#print(picdir)