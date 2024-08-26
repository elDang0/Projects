import sys,pygame as pyg,random
from pygame import *
import numpy as np
import heapq


#classes 
class node:
    linkedNodes = [None,None,None,None]
    viseted = False
    cordTopLeft = None
    cordBottomRight = None
    cordTopRight = None
    cordBottomLeft = None
    gridposX = None
    gridposY = None
    gridpos = None
    explored = None
    isNode = False
    def __init__(self,cordTopLeft):
        self.cordTopLeft = cordTopLeft

        self.cordBottomLeft = (cordTopLeft[0]+blockSize,cordTopLeft[1])
        self.cordBottomRight = (cordTopLeft[0]+blockSize,cordTopLeft[1]+blockSize)
        self.cordTopRight = (cordTopLeft[0],cordTopLeft[1]+blockSize)

        self.gridposX =  (self.cordTopLeft[1] / blockSize)
        self.gridposY =  (self.cordTopLeft[0] / blockSize)
        self.gridpos = self.gridposY,self.gridposX
        self.linkedNodes = [None,None,None,None]

        #solfe
        self.explored = False
        self.isNode = False
        self.d=float('inf')
        self.index_in_queue=None
#global vars
pyg.init()

valStack = []
exploreStack = []
viseted = 0
WINDOW_WITH = 1280
WINDOW_HIGHT = 720
SCREEN_SCALE = (WINDOW_WITH,WINDOW_HIGHT)
SCREEN = pyg.display.set_mode(SCREEN_SCALE)
clock = pyg.time.Clock()
backgroundcolor = "darkgray"
wallcolor = "darkgreen"
blockSize = 40
grid = []

#funks gen
def drawGrid():
    for row in range(0, WINDOW_WITH, blockSize):
        for colom in range(0, WINDOW_HIGHT, blockSize):
            rect = pyg.Rect(row, colom, blockSize, blockSize)
            pyg.draw.rect(SCREEN, backgroundcolor, rect, blockSize) # fill rect
            pyg.draw.rect(SCREEN, wallcolor, rect, 1) #draw border       
def initGridGrafick():
    for row in range(0, WINDOW_WITH, blockSize):
        grid.append([])
        for colom in range(0, WINDOW_HIGHT, blockSize):
            grid[int((row/blockSize))].append(node((row,colom)))
def drawMaze():
    startigpos = None
    for row in range(0, WINDOW_WITH, blockSize):
        for colom in range(0, WINDOW_HIGHT, blockSize):
            x = int((colom/blockSize))
            y = int((row/blockSize))
            if grid[y][x].linkedNodes[0] != None:
                startigpos = grid[y][x].cordTopLeft
                endingpos = grid[y][x].cordTopRight
                pyg.draw.line(SCREEN,backgroundcolor,startigpos,endingpos,3)
            if grid[y][x].linkedNodes[1] != None:
                startigpos = grid[y][x].cordTopRight
                endingpos = grid[y][x].cordBottomRight
                pyg.draw.line(SCREEN,backgroundcolor,startigpos,endingpos,3)
            if grid[y][x].linkedNodes[2] != None:
                startigpos = grid[y][x].cordBottomRight
                endingpos = grid[y][x].cordBottomLeft
                pyg.draw.line(SCREEN,backgroundcolor,startigpos,endingpos,3)
            if grid[y][x].linkedNodes[3] != None:
                startigpos = grid[y][x].cordBottomLeft
                endingpos = grid[y][x].cordTopLeft
                pyg.draw.line(SCREEN,backgroundcolor,startigpos,endingpos,3)
    pyg.draw.circle(SCREEN,"green",(blockSize/2,blockSize/2),blockSize/3)
    pyg.draw.circle(SCREEN,"red",(grid[-1][-1].cordTopLeft[0]+(blockSize/2),grid[-1][-1].cordTopLeft[1]+(blockSize/2)),blockSize/3)
def getNebors(node):
    valideNebors = []
    try:

        if not grid[int(node.gridposY-1)][int(node.gridposX)].viseted and grid[int(node.gridposY-1)][int(node.gridposX)].gridposY == node.gridposY-1 :
            valideNebors.append(grid[int(node.gridposY-1)][int(node.gridposX)])
        if not grid[int(node.gridposY)][int(node.gridposX+1)].viseted and grid[int(node.gridposY)][int(node.gridposX+1)].gridposX == node.gridposX+1:
            valideNebors.append(grid[int(node.gridposY)][int(node.gridposX+1)])
        if not grid[int(node.gridposY)][int(node.gridposX-1)].viseted and grid[int(node.gridposY)][int(node.gridposX-1)].gridposX == node.gridposX-1:
            valideNebors.append(grid[int(node.gridposY)][int(node.gridposX-1)])
        if not grid[int(node.gridposY+1)][int(node.gridposX)].viseted and grid[int(node.gridposY+1)][int(node.gridposX)].gridposY == node.gridposY+1:
            valideNebors.append(grid[int(node.gridposY+1)][int(node.gridposX)])
    except IndexError:
        pass
    return valideNebors
def genMaze(viseted):
    pos = grid[0][0]
    while viseted < ((WINDOW_WITH / blockSize ) * (WINDOW_HIGHT / blockSize))-1:
        
        pos.viseted = True
        
        valideNabors = getNebors(pos)
        if 0 < len(valideNabors):        
            if 1 < len(valideNabors): 
                valStack.append(pos)
                pos.isNode = True
            viseted += 1
            posNext = valideNabors[int(random.randint(1, len(valideNabors)))-1]
            if posNext.gridposY == pos.gridposY-1:
                pos.linkedNodes[0] = posNext
                posNext.linkedNodes[2] = pos
            elif posNext.gridposX == pos.gridposX+1:
                pos.linkedNodes[1] = posNext
                posNext.linkedNodes[3] = posNext
            elif posNext.gridposY == pos.gridposY+1:
                pos.linkedNodes[2] = posNext
                posNext.linkedNodes[0] = posNext
            elif posNext.gridposX == pos.gridposX-1:
                pos.linkedNodes[3] = posNext
                posNext.linkedNodes[1] = posNext
        else:
            while 0 == (len(valideNabors)):
                #if  valStack[-1] != None:
                    posNext = valStack[-1]
                    valStack.pop()
                    valideNabors = getNebors(posNext)
                
        pos = posNext

#funks solfe
def get_valPath(node):
    val = []
    for x in node.linkedNodes:
        if x != None:
            val.append(x)
    return val
def drawPath(): 
    for row in range(0, WINDOW_WITH, blockSize):
        for colom in range(0, WINDOW_HIGHT, blockSize):
            x = int((colom/blockSize))
            y = int((row/blockSize))
            if grid[y][x].explored:
                pyg.draw.circle(SCREEN,"blue",(colom+(blockSize/2),row+(blockSize/2)),blockSize/4,blockSize/4)   
def dfs():
      pos = grid[0][0]
      while pos.gridpos != grid[-1][-1].gridpos:
        
        pos.explored = True
        
        valideNabors = get_valPath(pos)
        if 0 < len(valideNabors):        
            if 1 < len(valideNabors): 
                valStack.append(pos)
            posNext = valideNabors[int(random.randint(1, len(valideNabors)))-1]
            #posNext = pos
        else:
            while 0 == (len(valideNabors)):
                posNext = exploreStack[-1]
                exploreStack.pop()
                valideNabors = get_valPath(posNext)
                
        pos = posNext
#init   
initGridGrafick()
genMaze(viseted)
drawGrid() 
drawMaze()
#dfs()
while True:  
    drawPath()

    for event in pyg.event.get():
        if event.type == QUIT: pyg.quit()

    pyg.display.flip()
    clock.tick(60)


            