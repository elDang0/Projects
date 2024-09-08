import sys,pygame as py,random,time
from pygame import *


#init
py.init()

WITH = 1280
HIGHT = 720
SCREENSCALE = WITH,HIGHT
SCREEN = py.display.set_mode(SCREENSCALE)

py.font.init()
FONT = py.font.SysFont("monospace", 50)

SCREEN.fill("black")

DWITH = WITH * (1/3)
GRIDRECT = (DWITH,0),(DWITH,HIGHT)

BLOCKRECT = (DWITH/10),(HIGHT/20)

#funcs
def DrawBlock(posWITH,posHIGHT):
    py.draw.rect(SCREEN,"red",(((DWITH+(DWITH/10)*posWITH),((HIGHT/20)*posHIGHT)),((DWITH/10),(HIGHT/20))))

def drawGrid():
    py.draw.rect(SCREEN,"white",GRIDRECT)
    x=0
    while x<=10:
        py.draw.line(SCREEN,"gray",(DWITH + (DWITH/10)*x,0),(DWITH + (DWITH/10)*x,HIGHT))
        x=x+1
    x=0
    while x<=20:
        py.draw.line(SCREEN,"gray",(DWITH,(HIGHT/20)*x),(DWITH*2,(HIGHT/20)*x))
        x=x+1

#logik

while True:  
    drawGrid()
    DrawBlock(0,10)

    for event in py.event.get():
        if event.type == QUIT: py.quit()

    py.display.flip()
    