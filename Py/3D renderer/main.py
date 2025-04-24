import pygame as pyg
import Renderer, object
from RendererStdClasses import *
from object import stdObjects

# consts
WINDOW_WITH = 1280
WINDOW_HIGHT = 720


#init
pyg.init()
clock = pyg.time.Clock()
display = pyg.display.set_mode((WINDOW_WITH,WINDOW_HIGHT))

renderer3D = Renderer.Renderer3D(WINDOW_WITH,WINDOW_HIGHT,display)

# Create a compound object example
cube1 = stdObjects.create_cube()
cube1.scale = 150
cube1.setColor((255, 100, 100))

pyramid1 = stdObjects.create_pyramid()
pyramid1.scale = 15
pyramid1.setColor((100, 255, 100))

# Combine cube and pyramid
offset = Point3D(0, 0, 0)  # Place pyramid 2 units to the right of cube
cube1.combine_with(pyramid1, offset)

renderer3D.add_object(cube1)  # Now contains both cube and pyramid as one object

diamond1 = stdObjects.create_diamond()
diamond1.scale = 15
diamond1.setColor((100, 100, 255))  # Blue

renderer3D.add_object(diamond1)

col = 0
#run
while True:  
    for event in pyg.event.get():
        if event.type == pyg.QUIT: pyg.quit()
    
    display.fill(pyg.Color(0,0,0))

    renderer3D.objects[0].rotateX(0.01)
    renderer3D.objects[0].rotateY(0.01)
    renderer3D.draw_object(0)
    
    clock.tick(60)
    pyg.display.flip()

