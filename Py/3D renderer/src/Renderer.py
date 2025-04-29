import pygame
from typing import List, Optional
from object import Object3D
from RendererStdClasses import Point2D, Point3D, Vertex

class Renderer3D:
    """3D renderer for managing and displaying 3D objects."""

    def __init__(self, window_width: int, window_height: int, screen: pygame.Surface, 
                 fov: float = 30.0, delta_time: float = 0.0):
        self.window_width = window_width
        self.window_height = window_height
        self.screen = screen
        self.fov = fov
        self.delta_time = delta_time
        self.objects: List[Object3D] = []

    def add_object(self, obj: Object3D) -> bool:
        """Add a 3D object to render."""
        if isinstance(obj, Object3D):
            self.objects.append(obj)
            return True
        raise TypeError("Object must be of type Object3D")

    def project_point(self, point: Point3D, scale: float, 
                     center_x: Optional[float] = None,
                     center_y: Optional[float] = None) -> Point2D:
        """Project 3D point to 2D screen coordinates."""
        center_x = center_x or self.window_width / 2
        center_y = center_y or self.window_height / 2
        
        z_factor = self.fov + point.z
        return Point2D(
            center_x + (self.fov * point.x) / z_factor * scale,
            center_y + (self.fov * point.y) / z_factor * scale
        )

    def draw_object(self, index: int) -> bool:
        """Draw a specific object by index."""
        try:
            obj = self.objects[index]
            for vertex in obj.vertex_arr:
                start_2d = self.project_point(vertex.start, obj.scale)
                end_2d = self.project_point(vertex.end, obj.scale)
                pygame.draw.line(self.screen, obj.color, 
                               (start_2d.x, start_2d.y),
                               (end_2d.x, end_2d.y), 5)
            return True
        except IndexError:
            print(f"Object at index {index} does not exist")
            return False

    def draw_all(self) -> None:
        """Draw all objects in the renderer."""
        for i in range(len(self.objects)):
            self.draw_object(i)