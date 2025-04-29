from numpy import cos, sin
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Point2D:
    """Represents a 2D point with x,y coordinates."""
    x: float = 0.0
    y: float = 0.0

@dataclass 
class Point3D:
    """Represents a 3D point with rotation capabilities."""
    x: float = 0.0
    y: float = 0.0 
    z: float = 0.0
    rotation_x: float = 0.0
    rotation_y: float = 0.0

    def rotate_x(self, phi: float) -> None:
        """Rotate point around X axis."""
        self.rotation_x += phi
        new_y = cos(phi) * self.y - sin(phi) * self.z
        new_z = sin(phi) * self.y + cos(phi) * self.z
        self.y, self.z = new_y, new_z

    def rotate_y(self, phi: float) -> None:
        """Rotate point around Y axis."""
        self.rotation_y += phi
        new_x = cos(phi) * self.x - sin(phi) * self.z
        new_z = sin(phi) * self.x + cos(phi) * self.z
        self.x, self.z = new_x, new_z

    def scale(self, scale: float) -> None:
        """Scale point coordinates."""
        factor = scale / 100
        self.x *= factor
        self.y *= factor
        self.z *= factor

@dataclass
class Vertex:
    """Represents a 3D vertex with start and end points."""
    start: Optional[Point3D] = None
    end: Optional[Point3D] = None

    def scale(self, scale: float) -> 'Vertex':
        """Scale the vertex."""
        if self.start and self.end:
            self.start.scale(scale)
            self.end.scale(scale)
        return self