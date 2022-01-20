#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont


epd = epd7in5_V2.EPD()
epd.init()
epd.Clear()

font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)


Limage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Limage)
draw.text((2, 0), 'hello world', font = font35, fill = 0)
epd.display(epd.getbuffer(Limage))
epd.sleep()
