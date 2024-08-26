import sys,pymunk,pygame as py
from pygame import *

#vars
screenWith = 1280                                                   #Screen Widh
screenHight = 720                                                   #screenHight
screenSCALE = screenWith,screenHight                                #Screen dimensions
DscreenWith = screenWith * (1/3)                                    #Screen With / 3 becouse only 1/3 is the are where the tiles wil be           
gridRect = (DscreenWith,0),(DscreenWith,screenHight)                
blockRect = (DscreenWith/10),(screenHight/20)
py.font.init()
FONT = py.font.SysFont("monospace", 50)


#init
py.init()                                                           #init pygame
clock = py.time.Clock()                                             #a clock
screen = py.display.set_mode(screenSCALE)                           #sets the screen sice to the screenScale variable
screen.fill("black")                                                #makes the screen black

space = pymunk.Space()
space.gravity= 0,500

TileWidth = 20                                                      #pixel sizes for grid squares
TileHeight = 20                                                    
TileMargin = 4                                                      

class MapTile(object):                                              #blocks
    def __init__(self, Name, Column, Row):
        self.Name = Name                                                      
        self.Column = Column                                                     
        self.Row = Row                                                     

#funcs
def DrawBlock(posscreenWith,posscreenHight):
    py.draw.rect(screen,"red",(((DscreenWith+(DscreenWith/10)*posscreenWith),((screenHight/20)*posscreenHight)),((DscreenWith/10),(screenHight/20))))

def drawGrid():
    py.draw.rect(screen,"white",gridRect)
    x=0
    while x<=10:
        py.draw.line(screen,"gray",(DscreenWith + (DscreenWith/10)*x,0),(DscreenWith + (DscreenWith/10)*x,screenHight))
        x=x+1
    x=0
    while x<=20:
        py.draw.line(screen,"gray",(DscreenWith,(screenHight/20)*x),(DscreenWith*2,(screenHight/20)*x))
        x=x+1

#logik

while True:  
    drawGrid()
    DrawBlock(0,10)

    for event in py.event.get():
        if event.type == QUIT: 
            py.quit()
            sys.exit()

    space.step(1/50)
    py.display.update()
    