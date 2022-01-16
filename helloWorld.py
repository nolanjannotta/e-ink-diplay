from PIL import Image,ImageDraw,ImageFont
from datetime import date, datetime
import time
import schedule
import epd7in5_V2
import logging
import os
import weather

picdir = "/home/pi/eInk/e-ink-display/pic"
fontdir = "/home/pi/eInk/e-ink-display/font"

monthFont = ImageFont.truetype(os.path.join(fontdir, 'OstrichSans-Black.ttf'),size=75)
dayFont = ImageFont.truetype(os.path.join(fontdir, 'OstrichSans-Black.ttf'),size=70)
weatherFont = ImageFont.truetype(os.path.join(fontdir, 'OpenSans-Regular.ttf'),size=40)
conditionFont = ImageFont.truetype(os.path.join(fontdir, 'OpenSans-Regular.ttf'),size=30)
timeFont = ImageFont.truetype(os.path.join(fontdir, 'OpenSans-Regular.ttf'),size=105)

sunFont = ImageFont.truetype(os.path.join(fontdir, 'OpenSans-Regular.ttf'),size=27)
epd = epd7in5_V2.EPD()

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

def draw():
    

    raw_time = datetime.now().time()
    time = raw_time.strftime("%I:%M %p")

    currentWeather = weather.Weather()

    today = date.today()
    monthDate = today.strftime("%B %d, %Y")
    day = today.strftime('%A')

    temp = f"{currentWeather.temp()} °F"

    sunset = f"Sunset: {currentWeather.sunset()}"
    sunrise = f"Sunrise: {currentWeather.sunrise()}"




    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)

    # draws day and date rectangle
    draw.rectangle((0, 0, 478, 200), outline = 0, width=2)
    draw.text((10, 17), day, fill = 0, font=monthFont)
    draw.text((10, 107), monthDate, fill = 0, font=dayFont)

    # draws weather rectangle
    draw.rectangle((0, 202, 238, 300), outline = 0, width=2)
    draw.text((10, 205), temp, fill = 0, font=weatherFont)
    draw.text((10, 248), currentWeather.description(), fill = 0, font=conditionFont)



    draw.rectangle((240, 202, 478, 300), outline = 0, width=2)

    draw.text((250, 211), sunrise, fill = 0, font=sunFont)
    draw.text((250, 252), sunset, fill = 0, font=sunFont)

    # draw clock
    draw.rectangle((0, 302, 478, 520), outline = 0, width=2)
    draw.text((10, 340), time, fill = 0, font=timeFont)

    epd.init()  
    epd.Clear()
    epd.display(epd.getbuffer(Himage))
    # time.sleep(2)

    # Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    # draw = ImageDraw.Draw(Limage)
    # draw.text((0, 0), "oi cunt", fill=0)
    # draw.text((0, 10), "whats poppin?", fill=0)
    # draw.text((0, 20), "brand new whip just hopped in", fill=0)
    # Lbuf = epd.getbuffer(Limage)
    # epd.display(Lbuf)
    # time.sleep(3)




    # Pimage = Image.open(os.path.join(picdir, 'panda.bmp'))
    # epd.display(epd.getbuffer(Pimage))
    # time.sleep(5)

    # logging.info("4.read bmp file on window")
    # Himage2 = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    # bmp = Image.open(os.path.join(picdir, 'newspaper.bmp'))
    # Himage2.paste(bmp, (50,10))
    # epd.display(epd.getbuffer(Himage2))
    # time.sleep(10)

    epd.sleep()

timer = Timer()
def main():
    
    
    draw()

    # schedule.every(1).minutes.do(draw)

    # clear the screen

    while True:
        if timer.checkUpdate:
            draw()

        time.sleep(1)

        
        # schedule.every(1).minutes.do(func)
        # draw()
        # time.sleep(60)
        # epd.init()  
        # epd.Clear()


        


    # Horizontal image
    # Himage = Image.new('1', (epd7in5_V2.EPD_WIDTH, epd7in5_V2.EPD_HEIGHT), 255)
    # draw = ImageDraw.Draw(Himage)
    # draw.text((0, 0), "hello world", fill=0)
    # draw.text((0, 10), "whats poppin?", fill=0)
    # draw.text((0, 20), "brand new whip just hopped in", fill=0)

    # Hbuf = epd.getbuffer(Himage)


    # # Display buffer
    # epd.display(Hbuf)

    # Set display in deep sleep
    # time.sleep(3)
    #Vertical image

    

if __name__ == "__main__":
    main()

