from datetime import datetime
import time

class Timer:
    def __init__(self):
        self.timer = self.now()
    def now(self):
        return int(time.time())
    def nextavailable(self):
        return int(time.time()) + 60
    def checkUpdate(self):
        if(self.timer >= self.nextavailable()):
            self.timer = self.now()
            return True

        

timer = Timer()

def func():
    time.sleep(2)
    print("hello")

def main():

    func()
    while True:

        if timer.checkUpdate:
            func()

        time.sleep(1)

if __name__ == "__main__":
    main()