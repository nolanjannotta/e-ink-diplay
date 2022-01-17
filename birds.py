from os import listdir
from os.path import isfile, join
import random



class Bird:

    def __init__(self):
        self.picdir = "/home/pi/eInk/e-ink-display/pic"

    def getRandomPic(self):
        pass
    def getAllPics(self):
        return  [f for f in listdir(self.picdir) if isfile(join(self.picdir, f))]
    def random_bird(self):
        return f"bird{random.randrange(1,5,1)}"

bird = Bird()

print (bird.random_bird())