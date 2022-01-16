from datetime import datetime
import time

class Timer:
    def __init__(self):
        self.timer = self.now()
    def now(self):
        return time.time().trunc()
    def nextavailable(self):
        return time.time().trunc() + 60
    def checkUpdate(self):
        if(self.timer >= self.nextavailable()):
            self.timer = self.now()
            return True

        

timer = Timer()

def func():
    print("hello")

def main():

    func()
    while True:
        if timer.checkUpdate:
            func()

        time.sleep(4)

