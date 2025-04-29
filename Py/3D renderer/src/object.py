from dataclasses import dataclass, field
from typing import List, Callable
import pygame as pyg
from RendererStdClasses import Point3D, Vertex

@dataclass
class Object3D:
    """3D object with vertices, rotation and scaling capabilities."""
    vertices: List[Vertex]  # Changed from vertex_arr to be more clear
    rotation_x: float = 0.0
    rotation_y: float = 0.0
    scale: float = 100.0
    color: str = "white"

    def __post_init__(self):
        """Ensure vertices is a list, not a function."""
        if callable(self.vertices):
            self.vertices = self.vertices()

    def scale_by(self, scale: float) -> None:
        """Increment scale by given amount."""
        self.scale += scale

    def scale_to(self, scale: float) -> None:
        """Set scale to specific value."""
        self.scale = scale

    def rotate_x(self, phi: float) -> None:
        """Rotate object around X axis."""
        self.rotation_x += phi
        for vertex in self.vertices:
            if vertex.start and vertex.end:
                vertex.start.rotate_x(phi)
                vertex.end.rotate_x(phi)

    def rotate_y(self, phi: float) -> None:
        """Rotate object around Y axis."""
        self.rotation_y += phi
        for vertex in self.vertices:
            if vertex.start and vertex.end:
                vertex.start.rotate_y(phi)
                vertex.end.rotate_y(phi)

    def update(self) -> None:
        """Update object state - rotate continuously."""
        self.rotate_y(0.02)
        self.rotate_x(0.02)

class StdObjects:
    """Standard 3D object definitions."""
    
    @staticmethod
    def cube() -> Object3D:
        """Create a cube object."""
        vertices = [
            Vertex(Point3D(-1, -1, -1), Point3D(1, -1, -1)),
            Vertex(Point3D(1, -1, -1), Point3D(1, 1, -1)),
            Vertex(Point3D(1, 1, -1), Point3D(-1, 1, -1)),
            Vertex(Point3D(-1, 1, -1), Point3D(-1, -1, -1)),
            Vertex(Point3D(-1, -1, 1), Point3D(1, -1, 1)),
            Vertex(Point3D(1, -1, 1), Point3D(1, 1, 1)),
            Vertex(Point3D(1, 1, 1), Point3D(-1, 1, 1)),
            Vertex(Point3D(-1, 1, 1), Point3D(-1, -1, 1)),
            Vertex(Point3D(-1, -1, -1), Point3D(-1, -1, 1)),
            Vertex(Point3D(1, -1, -1), Point3D(1, -1, 1)),
            Vertex(Point3D(1, 1, -1), Point3D(1, 1, 1)),
            Vertex(Point3D(-1, 1, -1), Point3D(-1, 1, 1))
        ]
        return Object3D(vertices=vertices)