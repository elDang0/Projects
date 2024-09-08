import tetris.tiles as tiles
from tetris.tiles import *

girdArry = []

x = 0
while x<=20:
    girdArry.append([0,0,0,0,0,0,0,0,0,0],)
    x +=1
#print(girdArry)

#gravety
class cord:
    x = 0
    y = 0
    val = 0

def grevetycheck(x,y):
    if girdArry[x][y-1] == 1:return False
    
def setXY(x,y,type):
    girdArry[x][y] = type

class block:
    Cords = cord(),cord(),cord(),cord()
    typ = 0
    til = tiles[typ][0] 

    def __init__(self,typ):
        self.typ = typ

    def fall(self):
        while True:
            for c in self.Cords:
                if not grevetycheck(c.x,c.y): 
                    for c in self.Cords: c.val = 1
                    break
            for c in self.Cords:
                c.y = c.y - 1


    
    