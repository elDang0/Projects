import pygame as pyg
from Vars import *

# consts
WINDOW_WITH = 1280
WINDOW_HIGHT = 720
Cube = [    Vertex(Point3D(-1,-1,-1),Point3D(1,-1,-1)),
            Vertex(Point3D(-1,-1,-1),Point3D(-1,-1,1)),
            Vertex(Point3D(-1,-1,-1),Point3D(-1,1,-1)),
            Vertex(Point3D(1,1,1),Point3D(1,1,-1)),
            Vertex(Point3D(1,1,1),Point3D(1,-1,1)),
            Vertex(Point3D(1,1,1),Point3D(-1,1,1)),
            Vertex(Point3D(-1,-1,1),Point3D(-1,1,1)),
            Vertex(Point3D(1,1,-1),Point3D(-1,1,-1)),
            Vertex(Point3D(1,-1,1),Point3D(-1,-1,1)),
            Vertex(Point3D(-1,1,-1),Point3D(-1,1,1)),
            Vertex(Point3D(1,1,-1),Point3D(1,-1,-1)),
            Vertex(Point3D(1,-1,1),Point3D(1,-1,-1)),
        ]

#init
pyg.init()
display = pyg.display.set_mode((WINDOW_WITH,WINDOW_HIGHT))
backgroundRect = pyg.Rect(0,0,WINDOW_WITH,WINDOW_HIGHT)
r = Renderer3D(WINDOW_WITH,WINDOW_HIGHT,display)
#run
while True:  
    for event in pyg.event.get():
        if event.type == pyg.QUIT: pyg.quit()
    
    pyg.draw.rect(display,"black", backgroundRect)
    r.rotation = r.rotation + 0.001
    r.draw3D(Cube)

    pyg.display.flip()




