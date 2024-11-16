from RendererStdClasses import *
import pygame as pyg

class Object3D:
    rotationX = 0.0
    rotationY = 0.0
    scale = 100.0
    vertexArr = []
    color = "white"
    connects = []
    allPoints = []

    def __init__(self,vertexArr = [],rotationX = 0.0,rotationY = 0.0,scale = 100.0):
        self.rotationX = rotationX
        self.rotationY = rotationY
        self.scale = scale
        self.vertexArr = vertexArr
    def scaleBy(self,scale):
        self.scale += scale
    def scaleTo(self,scale):
        self.scale = scale
    def rotateX(self,phi):# rotates the start and end point of a vertex
        self.rotationX +=  phi
        for i in range(self.vertexArr.__len__()):
            self.vertexArr[i].getPointStart().rotateX(phi)
            self.vertexArr[i].getPointEnd().rotateX(phi)
    def rotateY(self,phi): # rotates the start and end point of a vertex
        self.rotationY += phi
        for i in range(self.vertexArr.__len__()):
            self.vertexArr[i].getPointStart().rotateY(phi)
            self.vertexArr[i].getPointEnd().rotateY(phi) 
    def getRotationX(self):
        return self.rotationX %  6.285 # 6.285 is a whole rotation
    def getRotationY(self):
        return self.rotationY %  6.285 # 6.285 is a whole rotation
    def addVertex(self,v):
        self.vertexArr.append(v)
    def setColore(self,col):
        self.color = col
    def getConecktetPoints(self,cord):
        out = []
        for i in range(self.vertexArr.__len__()):
            start = self.vertexArr[i].getPointStart()
            end = self.vertexArr[i].getPointEnd()
            if start.x is cord[0] and start.y is cord[1] and start.z is cord[2]:
                out.append(Vertex(start,end))
            if end.x is cord[0] and end.y is cord[1] and end.z is cord[2]:
                out.append(Vertex(start,end))              
        self.connects.append(out)
        
    def update(self):
        self.allPoints = []
        for i in range(self.vertexArr.__len__()):
            self.allPoints.append(self.vertexArr[i].getPointStart())
            self.allPoints.append(self.vertexArr[i].getPointEnd())
        self.connects = []
        for p in self.allPoints:
            self.getConecktetPoints([p.x,p.y,p.z])

class stdObjects:
    cubeVertexArray = [     Vertex(Point3D(-1,-1,-1),Point3D(1,-1,-1)),
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
                            Vertex(Point3D(1,-1,1),Point3D(1,-1,-1))]
