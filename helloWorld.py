from PIL import Image, ImageDraw, ImageFilter
import time
import epd7in5_V2
import logging
import os
picdir = "/home/pi/eInk/e-ink-display/pic"
epd = epd7in5_V2.EPD()
epd.init()

# clear the screen
epd.Clear()


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

logging.info("1.Drawing on the Horizontal image...")
Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)
# draw.text((10, 0), 'hello world', fill = 0)
# draw.text((10, 20), '7.5inch e-Paper', fill = 0)
# draw.line((20, 50, 70, 100), fill = 0)
# draw.line((70, 50, 20, 100), fill = 0)
draw.rectangle((0, 0, 478, 200), outline = 0, width=2)
# draw.line((165, 50, 165, 100), fill = 0)
# draw.line((140, 75, 190, 75), fill = 0)
# draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
draw.rectangle((0, 202, 238, 100), outline = 0)
draw.rectangle((240, 202, 478, 100), outline = 0)
# draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
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