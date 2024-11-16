import pygame as pyg
import Renderer,object
from RendererStdClasses import *
from object import stdObjects

# consts
WINDOW_WITH = 1280
WINDOW_HIGHT = 720

cube1= object.Object3D(scale=150)
cube1.vertexArr = stdObjects.cubeVertexArray


#init
pyg.init()
clock = pyg.time.Clock()
display = pyg.display.set_mode((WINDOW_WITH,WINDOW_HIGHT))

renderer3D = Renderer.Renderer3D(WINDOW_WITH,WINDOW_HIGHT,display)
renderer3D.addObject(cube1)

col = 0
#run
while True:  
    for event in pyg.event.get():
        if event.type == pyg.QUIT: pyg.quit()
    
    display.fill(pyg.Color(0,0,0))

    renderer3D.objects[0].
    renderer3D.fillObject(0)
    renderer3D.drawAll()
    
    
    clock.tick(60)
    pyg.display.flip()

