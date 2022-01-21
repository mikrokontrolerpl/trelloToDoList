import trelloParsers

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont

f = open('keys.dat')
KEY = str(f.readline()).strip()
TOKEN = str(f.readline()).strip()
BOARD = str(f.readline()).strip()
f.close()
url = 'https://api.trello.com/1/boards/'+BOARD+'/lists?cards=open&key='+KEY+'&token='+TOKEN
cards = trelloParsers.getCardsFromURL(url)
lista = cards.get("Do zrobienia")

file = open("log.txt", "w")
for x in lista:
	file.writelines(x)
	file.write("\n")
file.close()

file = open("log.txt", "r")
readlist = list()
for x in range(5):
	readlist.append(file.readline().strip())
file.close()

print (lista)
print (readlist)

epd = epd7in5_V2.EPD()
epd.init()
epd.Clear()

font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)


Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Limage)
draw.text((2, 0), 'hello world', font = font35, fill = 0)
epd.display(epd.getbuffer(Limage))
epd.sleep()
