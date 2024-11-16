from numpy import cos,sin

class Point2D:
    x : float = float()
    y : float = float()

    def __init__(self,x=None,y=None):
        self.x = x
        self.y = y

class Point3D:
    x : float  = float()
    y : float = float()
    z : float = float()
    rotationY : float  = 0.0
    rotationX : float  = 0.0

    def __init__(self,x=None,y=None,z=None):
        self.x = x
        self.y = y
        self.z = z
    def setArr(self,arr):
        self.x = arr[0]
        self.y = arr[1]
        self.z = arr[2]
    def rotateX(self,phi):
        rPoint = Point3D()
        self.rotationX += phi
        rPoint.y = cos(phi) * self.y - sin(phi) * self.z
        rPoint.z = sin(phi) * self.y + cos(phi) * self.z

        self.y = rPoint.y
        self.z = rPoint.z
    def rotateY(self,phi):
        rPoint = Point3D()
        self.rotationY += phi

        rPoint.x = cos(phi) * self.x - sin(phi) * self.z
        rPoint.z = sin(phi) * self.x + cos(phi) * self.z

        self.x = rPoint.x
        self.z = rPoint.z
    def scalePoint(self,scale):
        self.x = self.x * scale /100
        self.y = self.y * scale /100
        self.z = self.z * scale /100
    def toArray(self):
        return [self.x,self.y,self.z]

class Vertex:
    end : Point3D = Point3D()
    start : Point3D = Point3D()
    
    def __init__(self,start=None,end=None):
        self.start = start
        self.end = end
    def getPoints(self):
        return [self.start,self.end]    
    def setPoints(self,arr):
        self.start = arr[0]
        self.end = arr[1]   
    def getPointEnd(self):
        return self.end
    def getPointStart(self):
        return self.start
    def scaleVertex(self,scale):
        self.start.scalePoint(scale)
        self.end.scalePoint(scale)
        return self

class muliVektor:
    VectorArr = []
