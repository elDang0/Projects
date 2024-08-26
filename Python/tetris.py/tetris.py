from settings import *
from pygame import *

class Block(object):                                              #blocks
    def __init__(self,):                                                    
        self

class Tile(object):                                              #Tile
    def __init__(self,):                                                    
        self

#funcs
def DrawBlock(posscreenWith,posscreenHight,screen):
    py.draw.rect(screen,"red",(((DscreenWith+(DscreenWith/10)*posscreenWith),((screenHight/20)*posscreenHight)),((DscreenWith/10),(screenHight/20))))

def drawGrid(screen):
    py.draw.rect(screen,"white",gridRect)
    x=0
    while x<=10:
        py.draw.line(screen,"gray",(DscreenWith + (DscreenWith/10)*x,0),(DscreenWith + (DscreenWith/10)*x,screenHight))
        x=x+1
    x=0
    while x<=20:
        py.draw.line(screen,"gray",(DscreenWith,(screenHight/20)*x),(DscreenWith*2,(screenHight/20)*x))
        x=x+1
