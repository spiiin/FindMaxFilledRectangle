import numpy
from PIL import Image, ImageDraw
from random import randint

def drawRandomEllipse(draw):
    x,y = randint(0, 256), randint(0, 256)
    w,h = randint(16, 64), randint(16, 64)
    draw.ellipse((x,y,x+w,y+h), fill="green", outline="black")
 
def generate((w,h)):
    image = Image.new("RGB", (w,h), (255,255,255))
    draw = ImageDraw.Draw(image)
    for i in xrange(32):
        drawRandomEllipse(draw)
    return image
    