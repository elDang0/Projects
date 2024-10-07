import numpy as np
from numpy import cos,sin
import pygame

def Rx(phi):
    return np.array([1,0,0],
                    [0,cos(phi),sin(phi)],
                    [0,sin(phi),cos(phi)])
                    

def Ry(phi):
    return np.array([cos(phi),0,sin(phi)],
                    [0,1,0],
                    [-sin(phi),0,cos(phi)])

def Rz(phi):
    return np.array([cos(phi),-sin(phi),0],
                    [sin(phi),cos(phi),0],
                    [0,0,1])


class Point2D:
    x = int
    y = int

    def __init__(self,x,y):
        self.x = x
        self.y = y

class Point3D:
    x = int
    y = int
    z = int

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Vertex:
    end = Point3D
    start = Point3D
    
    def __init__(self,a,b):
        self.start = a
        self.end = b

class Renderer3D:
    rotation = float(0.1)
    FOV = 30.0
    deltaTime = 0.0
    windowWith = int
    windowHight = int
    screen = pygame.surface

    def __init__(self,windowWith,windowHight,screen):
        self.windowWith = windowWith
        self.windowHight = windowHight
        self.screen = screen

    def roate(self,point):
        tempPoint = Point3D
        rPoint = Point3D
        tempPoint.x = point.x
        tempPoint.y = cos(self.rotation) * point.y - sin(self.rotation) * point.z
        tempPoint.z = sin(self.rotation) * point.y + cos(self.rotation) * point.z

        rPoint.x = cos(self.rotation) * tempPoint.x - sin(self.rotation) * tempPoint.z
        rPoint.y = tempPoint.y
        rPoint.z = sin(self.rotation) * tempPoint.x + cos(self.rotation) * tempPoint.z

        return rPoint
    def draw2D(self,v):
            pygame.draw.line(self.screen,"white",(v.start.x,v.start.y),(v.end.x,v.end.y),5)

    def projection(self,point):
        return Point2D(self.windowWith/2+(self.FOV * point.x)/(self.FOV + point.z)*100, self.windowHight/2+(self.FOV * point.y)/(self.FOV + point.z)*100,)
    
    def draw3D(self,Varr):
        for v in Varr:
            self.draw2D(Vertex(self.projection(self.roate(v.start)),self.projection(self.roate(v.end))))
        