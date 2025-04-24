from RendererStdClasses import Point3D, Vertex, Face
import pygame as pyg
from typing import List, Optional
from math import pi, cos, sin

class Object3D:
    """
    Represents a 3D object with vertices, rotation, scale, and color.
    Provides methods for transformations and updates.
    """
    def __init__(self, vertexArr: Optional[List[Vertex]] = None, faces: Optional[List[Face]] = None, 
                 rotationX: float = 0.0, rotationY: float = 0.0, scale: float = 100.0):
        self.rotationX: float = rotationX
        self.rotationY: float = rotationY
        self.scale: float = scale
        self.vertexArr: List[Vertex] = vertexArr if vertexArr else []
        self.color: str = "white"
        self.connects: List[List[Vertex]] = []
        self.allPoints: List[Point3D] = []
        self.faces: List[Face] = faces if faces else []
        self.is_filled: bool = True  # Default to filled

    def scaleBy(self, scale: float) -> None:
        """Increases the scale of the object by the given value."""
        self.scale += scale

    def scaleTo(self, scale: float) -> None:
        """Sets the scale of the object to the given value."""
        self.scale = scale

    def _update_faces_from_vertices(self) -> None:
        """Update face points to match vertex positions"""
        vertex_points = {}  # cache for unique points
        # First collect all unique points from vertices
        for vertex in self.vertexArr:
            start = vertex.getPointStart()
            end = vertex.getPointEnd()
            vertex_points[f"{start.x},{start.y},{start.z}"] = start
            vertex_points[f"{end.x},{end.y},{end.z}"] = end
        
        # Update face points to match vertex points
        for face in self.faces:
            for i, point in enumerate(face.points):
                key = f"{round(point.x,6)},{round(point.y,6)},{round(point.z,6)}"
                if key in vertex_points:
                    face.points[i] = vertex_points[key]

    def _make_unified_rotation(self, phi_x: float = 0, phi_y: float = 0) -> None:
        """Apply unified rotation to all points, keeping faces and vertices in sync"""
        # First rotate vertex points
        for vertex in self.vertexArr:
            if phi_x != 0:
                vertex.getPointStart().rotateX(phi_x)
                vertex.getPointEnd().rotateX(phi_x)
            if phi_y != 0:
                vertex.getPointStart().rotateY(phi_y)
                vertex.getPointEnd().rotateY(phi_y)

        # Create lookup of rotated points
        point_map = {}
        for vertex in self.vertexArr:
            start = vertex.getPointStart()
            end = vertex.getPointEnd()
            point_map[f"{round(start.x,6)},{round(start.y,6)},{round(start.z,6)}"] = start
            point_map[f"{round(end.x,6)},{round(end.y,6)},{round(end.z,6)}"] = end

        # Update face points to match rotated vertices
        for face in self.faces:
            for i, point in enumerate(face.points):
                key = f"{round(point.x,6)},{round(point.y,6)},{round(point.z,6)}"
                if key in point_map:
                    face.points[i] = point_map[key]

    def rotateX(self, phi: float) -> None:
        """Rotates the object around the X-axis"""
        self.rotationX += phi
        for vertex in self.vertexArr:
            vertex.getPointStart().rotateX(phi)
            vertex.getPointEnd().rotateX(phi)
        for face in self.faces:
            for point in face.points:
                point.rotateX(phi)

    def rotateY(self, phi: float) -> None:
        """Rotates the object around the Y-axis"""
        self.rotationY += phi
        for vertex in self.vertexArr:
            vertex.getPointStart().rotateY(phi)
            vertex.getPointEnd().rotateY(phi)
        for face in self.faces:
            for point in face.points:
                point.rotateY(phi)

    def getRotationX(self) -> float:
        """Returns the rotation around the X-axis, normalized to a full rotation (2π)."""
        return self.rotationX % 2*pi  

    def getRotationY(self) -> float:
        """Returns the rotation around the Y-axis, normalized to a full rotation (2π)."""
        return self.rotationY % 2*pi  

    def addVertex(self, v: Vertex) -> None:
        """Adds a vertex to the object."""
        self.vertexArr.append(v)

    def setColor(self, col: str) -> None:
        """Sets the color of the object."""
        self.color = col

    def getConnectedPoints(self, cord: List[float]) -> None:
        """
        Finds and stores all vertices connected to a given point.
        """
        out: List[Vertex] = []
        for vertex in self.vertexArr:
            start = vertex.getPointStart()
            end = vertex.getPointEnd()
            if [start.x, start.y, start.z] == cord:
                out.append(Vertex(start, end))
            if [end.x, end.y, end.z] == cord:
                out.append(Vertex(start, end))
        self.connects.append(out)

    def update(self) -> None:
        """
        Updates the list of all points and connected vertices for the object.
        """
        self.allPoints = []
        for vertex in self.vertexArr:
            self.allPoints.append(vertex.getPointStart())
            self.allPoints.append(vertex.getPointEnd())
        self.connects = []
        for point in self.allPoints:
            self.getConnectedPoints([point.x, point.y, point.z])

    def combine_with(self, other: 'Object3D', offset: Point3D = Point3D(0, 0, 0)) -> None:
        """
        Combines another object with this one, maintaining relative scales.
        
        Args:
            other: The Object3D to combine with this one
            offset: Optional Point3D representing the position offset for the added object
        """
        # Calculate scale ratio between objects
        scale_ratio = other.scale / self.scale
        
        # Add vertices with offset and scaled positions
        for vertex in other.vertexArr:
            new_start = Point3D(
                vertex.getPointStart().x * scale_ratio + offset.x,
                vertex.getPointStart().y * scale_ratio + offset.y,
                vertex.getPointStart().z * scale_ratio + offset.z
            )
            new_end = Point3D(
                vertex.getPointEnd().x * scale_ratio + offset.x,
                vertex.getPointEnd().y * scale_ratio + offset.y,
                vertex.getPointEnd().z * scale_ratio + offset.z
            )
            self.vertexArr.append(Vertex(new_start, new_end))

        # Add faces with offset and scaled positions
        for face in other.faces:
            new_points = []
            for point in face.points:
                new_point = Point3D(
                    point.x * scale_ratio + offset.x,
                    point.y * scale_ratio + offset.y,
                    point.z * scale_ratio + offset.z
                )
                new_points.append(new_point)
            self.faces.append(Face(new_points))

        # Update the object's state
        self.update()

class stdObjects:
    """
    A collection of standard 3D objects.
    """
    cubeVertexArray: List[Vertex] = [
        Vertex(Point3D(-1, -1, -1), Point3D(1, -1, -1)),
        Vertex(Point3D(-1, -1, -1), Point3D(-1, -1, 1)),
        Vertex(Point3D(-1, -1, -1), Point3D(-1, 1, -1)),
        Vertex(Point3D(1, 1, 1), Point3D(1, 1, -1)),
        Vertex(Point3D(1, 1, 1), Point3D(1, -1, 1)),
        Vertex(Point3D(1, 1, 1), Point3D(-1, 1, 1)),
        Vertex(Point3D(-1, -1, 1), Point3D(-1, 1, 1)),
        Vertex(Point3D(1, 1, -1), Point3D(-1, 1, -1)),
        Vertex(Point3D(1, -1, 1), Point3D(-1, -1, 1)),
        Vertex(Point3D(-1, 1, -1), Point3D(-1, 1, 1)),
        Vertex(Point3D(1, 1, -1), Point3D(1, -1, -1)),
        Vertex(Point3D(1, -1, 1), Point3D(1, -1, -1)),
    ]

    @staticmethod
    def create_pyramid() -> Object3D:
        """Creates a pyramid with a square base and triangular sides"""
        # Create base points
        points = [
            Point3D(0, 1, 0),     # 0: top point
            Point3D(-1, -1, -1),  # 1: front left
            Point3D(1, -1, -1),   # 2: front right
            Point3D(1, -1, 1),    # 3: back right
            Point3D(-1, -1, 1),   # 4: back left
        ]

        # Create vertices using point copies
        vertices = [
            # Base edges
            Vertex(Point3D(points[1].x, points[1].y, points[1].z), Point3D(points[2].x, points[2].y, points[2].z)),
            Vertex(Point3D(points[2].x, points[2].y, points[2].z), Point3D(points[3].x, points[3].y, points[3].z)),
            Vertex(Point3D(points[3].x, points[3].y, points[3].z), Point3D(points[4].x, points[4].y, points[4].z)),
            Vertex(Point3D(points[4].x, points[4].y, points[4].z), Point3D(points[1].x, points[1].y, points[1].z)),
            # Edges to top
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[1].x, points[1].y, points[1].z)),
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[2].x, points[2].y, points[2].z)),
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[3].x, points[3].y, points[3].z)),
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[4].x, points[4].y, points[4].z)),
        ]

        faces = [
            # Base
            Face([Point3D(points[1].x, points[1].y, points[1].z),
                 Point3D(points[2].x, points[2].y, points[2].z),
                 Point3D(points[3].x, points[3].y, points[3].z),
                 Point3D(points[4].x, points[4].y, points[4].z)]),
            # Sides
            Face([Point3D(points[0].x, points[0].y, points[0].z),
                 Point3D(points[1].x, points[1].y, points[1].z),
                 Point3D(points[2].x, points[2].y, points[2].z)]),
            Face([Point3D(points[0].x, points[0].y, points[0].z),
                 Point3D(points[2].x, points[2].y, points[2].z),
                 Point3D(points[3].x, points[3].y, points[3].z)]),
            Face([Point3D(points[0].x, points[0].y, points[0].z),
                 Point3D(points[3].x, points[3].y, points[3].z),
                 Point3D(points[4].x, points[4].y, points[4].z)]),
            Face([Point3D(points[0].x, points[0].y, points[0].z),
                 Point3D(points[4].x, points[4].y, points[4].z),
                 Point3D(points[1].x, points[1].y, points[1].z)])
        ]

        return Object3D(vertexArr=vertices, faces=faces)

    @staticmethod
    def create_diamond() -> Object3D:
        """Creates a diamond (octahedron) shape"""
        points = [
            Point3D(0, 1, 0),     # 0: top point
            Point3D(0, -1, 0),    # 1: bottom point
            Point3D(1, 0, 0),     # 2: right point
            Point3D(-1, 0, 0),    # 3: left point
            Point3D(0, 0, 1),     # 4: front point
            Point3D(0, 0, -1),    # 5: back point
        ]

        vertices = [
            # Middle cross
            Vertex(Point3D(points[3].x, points[3].y, points[3].z), Point3D(points[2].x, points[2].y, points[2].z)),
            Vertex(Point3D(points[5].x, points[5].y, points[5].z), Point3D(points[4].x, points[4].y, points[4].z)),
            # Top pyramid edges
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[2].x, points[2].y, points[2].z)),
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[3].x, points[3].y, points[3].z)),
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[4].x, points[4].y, points[4].z)),
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[5].x, points[5].y, points[5].z)),
            # Bottom pyramid edges
            Vertex(Point3D(points[1].x, points[1].y, points[1].z), Point3D(points[2].x, points[2].y, points[2].z)),
            Vertex(Point3D(points[1].x, points[1].y, points[1].z), Point3D(points[3].x, points[3].y, points[3].z)),
            Vertex(Point3D(points[1].x, points[1].y, points[1].z), Point3D(points[4].x, points[4].y, points[4].z)),
            Vertex(Point3D(points[1].x, points[1].y, points[1].z), Point3D(points[5].x, points[5].y, points[5].z))
        ]

        faces = [
            # Top faces
            Face([Point3D(points[0].x, points[0].y, points[0].z),
                 Point3D(points[2].x, points[2].y, points[2].z),
                 Point3D(points[4].x, points[4].y, points[4].z)]),
            Face([Point3D(points[0].x, points[0].y, points[0].z),
                 Point3D(points[4].x, points[4].y, points[4].z),
                 Point3D(points[3].x, points[3].y, points[3].z)]),
            Face([Point3D(points[0].x, points[0].y, points[0].z),
                 Point3D(points[3].x, points[3].y, points[3].z),
                 Point3D(points[5].x, points[5].y, points[5].z)]),
            Face([Point3D(points[0].x, points[0].y, points[0].z),
                 Point3D(points[5].x, points[5].y, points[5].z),
                 Point3D(points[2].x, points[2].y, points[2].z)]),
            # Bottom faces
            Face([Point3D(points[1].x, points[1].y, points[1].z),
                 Point3D(points[4].x, points[4].y, points[4].z),
                 Point3D(points[2].x, points[2].y, points[2].z)]),
            Face([Point3D(points[1].x, points[1].y, points[1].z),
                 Point3D(points[3].x, points[3].y, points[3].z),
                 Point3D(points[4].x, points[4].y, points[4].z)]),
            Face([Point3D(points[1].x, points[1].y, points[1].z),
                 Point3D(points[5].x, points[5].y, points[5].z),
                 Point3D(points[3].x, points[3].y, points[3].z)]),
            Face([Point3D(points[1].x, points[1].y, points[1].z),
                 Point3D(points[2].x, points[2].y, points[2].z),
                 Point3D(points[5].x, points[5].y, points[5].z)])
        ]

        return Object3D(vertexArr=vertices, faces=faces)

    @staticmethod
    def create_cube() -> Object3D:
        # Create all points first
        points = [
            Point3D(-1, -1, -1),  # 0 front bottom left
            Point3D(1, -1, -1),   # 1 front bottom right
            Point3D(1, 1, -1),    # 2 front top right
            Point3D(-1, 1, -1),   # 3 front top left
            Point3D(-1, -1, 1),   # 4 back bottom left
            Point3D(1, -1, 1),    # 5 back bottom right
            Point3D(1, 1, 1),     # 6 back top right
            Point3D(-1, 1, 1),    # 7 back top left
        ]
        
        # Create vertices using direct point references
        vertices = [
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[1].x, points[1].y, points[1].z)),  # front bottom
            Vertex(Point3D(points[1].x, points[1].y, points[1].z), Point3D(points[2].x, points[2].y, points[2].z)),  # front right
            Vertex(Point3D(points[2].x, points[2].y, points[2].z), Point3D(points[3].x, points[3].y, points[3].z)),  # front top
            Vertex(Point3D(points[3].x, points[3].y, points[3].z), Point3D(points[0].x, points[0].y, points[0].z)),  # front left
            Vertex(Point3D(points[4].x, points[4].y, points[4].z), Point3D(points[5].x, points[5].y, points[5].z)),  # back bottom
            Vertex(Point3D(points[5].x, points[5].y, points[5].z), Point3D(points[6].x, points[6].y, points[6].z)),  # back right
            Vertex(Point3D(points[6].x, points[6].y, points[6].z), Point3D(points[7].x, points[7].y, points[7].z)),  # back top
            Vertex(Point3D(points[7].x, points[7].y, points[7].z), Point3D(points[4].x, points[4].y, points[4].z)),  # back left
            Vertex(Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[4].x, points[4].y, points[4].z)),  # left bottom
            Vertex(Point3D(points[1].x, points[1].y, points[1].z), Point3D(points[5].x, points[5].y, points[5].z)),  # right bottom
            Vertex(Point3D(points[2].x, points[2].y, points[2].z), Point3D(points[6].x, points[6].y, points[6].z)),  # right top
            Vertex(Point3D(points[3].x, points[3].y, points[3].z), Point3D(points[7].x, points[7].y, points[7].z)),  # left top
        ]
        
        # Create faces using copies of points
        faces = [
            Face([Point3D(points[0].x, points[0].y, points[0].z), Point3D(points[1].x, points[1].y, points[1].z),
                 Point3D(points[2].x, points[2].y, points[2].z), Point3D(points[3].x, points[3].y, points[3].z)]),  # front
            Face([Point3D(points[5].x, points[5].y, points[5].z), Point3D(points[4].x, points[4].y, points[4].z),
                 Point3D(points[7].x, points[7].y, points[7].z), Point3D(points[6].x, points[6].y, points[6].z)]),  # back
            Face([Point3D(points[4].x, points[4].y, points[4].z), Point3D(points[0].x, points[0].y, points[0].z),
                 Point3D(points[3].x, points[3].y, points[3].z), Point3D(points[7].x, points[7].y, points[7].z)]),  # left
            Face([Point3D(points[1].x, points[1].y, points[1].z), Point3D(points[5].x, points[5].y, points[5].z),
                 Point3D(points[6].x, points[6].y, points[6].z), Point3D(points[2].x, points[2].y, points[2].z)]),  # right
            Face([Point3D(points[3].x, points[3].y, points[3].z), Point3D(points[2].x, points[2].y, points[2].z),
                 Point3D(points[6].x, points[6].y, points[6].z), Point3D(points[7].x, points[7].y, points[7].z)]),  # top
            Face([Point3D(points[4].x, points[4].y, points[4].z), Point3D(points[5].x, points[5].y, points[5].z),
                 Point3D(points[1].x, points[1].y, points[1].z), Point3D(points[0].x, points[0].y, points[0].z)]),  # bottom
        ]
        
        return Object3D(vertexArr=vertices, faces=faces)
