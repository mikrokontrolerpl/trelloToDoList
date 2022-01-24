#!usr/bin/python3
#import libraries
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

#import Trello credentials
file = open("keys.dat", "r")
KEY = str(file.readline()).strip()
TOKEN = str(file.readline()).strip()
BOARD_ID = str(file.readline()).strip()
BOARD_NAME = str(file.readline()).strip()
file.close()

#get current cards values
url = 'https://api.trello.com/1/boards/'+BOARD_ID+'/lists?cards=open&key='+KEY+'&token='+TOKEN
cards = trelloParsers.getCardsFromURL(url)
cardsList = cards.get(BOARD_NAME)

#import last card values
file = open("log.txt", "r")
lastCards = int(file.readline().strip())
readlist = list()
for x in cardsList:
	readlist.append(file.readline().strip())
file.close()

print (len(cardsList))
print (lastCards)
print (cardsList)
print (readlist)

#checking if cards changed
listchange = 0
if lastCards == len(cardsList):
    y = 0
    for x in cardsList:
        if cardsList[y] != readlist[y]:
            listchange = 1
        y += 1
else:
    listchange  = 1
    
print (listchange)

if listchange == 1:
    epd = epd7in5_V2.EPD()
    epd.init()
    epd.Clear()
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Limage)
    y = 0
    for x in cardsList:
        draw.text((2, y), x, font = font35, fill = 0)
        y += 38
    epd.display(epd.getbuffer(Limage))
    epd.sleep()
#export current card values
    file = open("log.txt", "w")
    file.write(str(len(cardsList)))
    file.write("\n")
    for x in cardsList:
        file.writelines(x)
        file.write("\n")
    file.close()
