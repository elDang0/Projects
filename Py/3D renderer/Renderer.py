import pygame,object
from RendererStdClasses import *

class Renderer3D: # contains Helpful Functions to render Objects and has some vars to give to objects
    objects = [] # stores all the objects assined to this Renderer

    def __init__(self,windowWith,windowHight,screen,FOV=30.0,deltaTime = 0.0):
        self.windowWith = windowWith
        self.windowHight = windowHight
        self.screen = screen
        self.FOV = FOV
        self.deltaTime = deltaTime       
    def addObject(self,obj):
        if type(obj) is object.Object3D: # only adds objects 
            self.objects.append(obj)
            return True
        else:
            print("in addObject: obj has to be an object type")
            return False
    def draw2D(self,v,color):
        if type(v) is Vertex:
            pygame.draw.line(self.screen,color,(v.start.x,v.start.y),(v.end.x,v.end.y),5)
        else:
            print("in Draw2D: v has to be a vertex type")
    def drawPoly2D(self,vArr,color):  
            cords = ()    
            for v in vArr:
                cords.__add__((v.end.x,v.end.y),(v.start.x,v.start.y))
            
            pygame.draw.polygon(self.screen,color,cords,0)

    def projection(self,point,scale,absX =None,absY = None): # converts a Point3D into a Point2D by projecting it onto a 2D screen
        if absY is None: absY = self.windowHight/2
        if absX is None: absX = self.windowWith/2
        return Point2D(absX+(self.FOV * point.x)/(self.FOV + point.z)*scale, absY+(self.FOV * point.y)/(self.FOV + point.z)*scale)  
    def drawObject(self,ob):
        color = self.objects[ob].color
        if ob <= self.objects.__len__() and ob >= 0:   
            for v in self.objects[ob].vertexArr:
                points = v.getPoints()               
                self.draw2D(Vertex(self.projection(points[0],self.objects[ob].scale),self.projection(points[1],self.objects[ob].scale)),color)
            return True
        else: 
            print("in drawObject: object at: " + str(ob) + "\n dose not exist")
            return False
    def drawAll(self):
        for i in range(self.objects.__len__()):
            self.drawObject(i)
    def fillObject(self,obj):# https://www.geeksforgeeks.org/pygame-drawing-objects-and-shapes/
        color = self.objects[obj].color
        if obj <= self.objects.__len__() and obj >= 0:   
            for v in self.objects[obj].vertexArr:
                points = v.getPoints()               
                self.draw2D(Vertex(self.projection(points[0],self.objects[obj].scale),self.projection(points[1],self.objects[obj].scale)),color)
            return True
        else: 
            print("in fillObject: object at: " + str(obj) + "\n dose not exist")
            return False
    