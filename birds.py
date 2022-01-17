from os import listdir
from os.path import isfile, join



class Bird:

    def __init__(self):
        self.picdir = "/home/pi/eInk/e-ink-display/pic"

    def getRandomPic(self):
        pass
    def getAllPics(self):
        return  [f for f in listdir(self.picdir) if isfile(join(self.picdir, f))]

bird = Bird()

print (bird.getAllPics())