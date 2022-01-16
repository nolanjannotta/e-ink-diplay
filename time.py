from datetime import datetime
import time

class Timer:
    def __init__(self):
        self.timer = self.now()
    def now(self):
        return int(time.time())
    def nextavailable(self):
        return self.timer + 60

    def checkUpdate(self):
        if(self.now >= self.nextavailable()):
            self.timer = self.now()
            return True
        pass
        

timer = Timer()

def func():
    print(timer.timer)
    print(timer.nextavailable())
    print(timer.now())
    print("hello")

def main():

    func()
    while True:

        if timer.checkUpdate:
            func()

        time.sleep(1)

if __name__ == "__main__":
    main()