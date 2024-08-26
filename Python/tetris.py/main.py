import tetris,sys,pymunk,pygame as py
from pygame import *
from settings import *

#init
py.init()                                                           #init pygame
py.font.init()
clock = py.time.Clock()                                             #a clock
screen = py.display.set_mode(screenSCALE)                           #sets the screen sice to the screenScale variable
screen.fill("black")                                                #makes the screen black
                                           


while True:                                                         #logik
    tetris.drawGrid(screen)
    tetris.DrawBlock(0,10,screen)

    for event in py.event.get():
        if event.type == QUIT: 
            py.quit()
            sys.exit()


    py.display.update()
    