import pygame
from typing import List, Optional
from object import Object3D
from RendererStdClasses import Vertex, Point2D, Point3D

class Renderer3D:
    """
    A 3D renderer class that handles the projection and drawing of 3D objects onto a 2D screen.
    Contains helper functions to render Objects and maintains rendering state.
    """
    def __init__(self, window_width: int, window_height: int, screen: pygame.Surface, 
                 fov: float = 30.0, delta_time: float = 0.0) -> None:
        """
        Initialize the renderer with screen dimensions and rendering parameters.

        Args:
            window_width: Width of the rendering window in pixels
            window_height: Height of the rendering window in pixels
            screen: Pygame surface to draw on
            fov: Field of view angle in degrees
            delta_time: Time delta for animations
        """
        self.window_width = window_width
        self.window_height = window_height
        self.screen = screen
        self.FOV = fov
        self.delta_time = delta_time
        self.objects: List[Object3D] = []

    def add_object(self, obj: Object3D) -> bool:
        """
        Add a 3D object to the renderer.

        Args:
            obj: Object3D instance to be added

        Returns:
            bool: True if object was added successfully, False otherwise
        """
        if isinstance(obj, Object3D):
            self.objects.append(obj)
            return True
        print("Error in add_object: obj must be an Object3D type")
        return False

    def draw_2d(self, vertex: Vertex, color: tuple[int, int, int]) -> None:
        """
        Draw a 2D line segment on the screen.

        Args:
            vertex: Vertex containing start and end points
            color: RGB color tuple
        """
        if isinstance(vertex, Vertex):
            pygame.draw.line(self.screen, color,
                           (vertex.start.x, vertex.start.y),
                           (vertex.end.x, vertex.end.y), 5)
        else:
            print("Error in draw_2d: vertex must be a Vertex type")

    def draw_poly_2d(self, vertices: List[Vertex], color: tuple[int, int, int]) -> None:
        """
        Draw a filled 2D polygon from vertices.

        Args:
            vertices: List of vertices forming the polygon
            color: RGB color tuple
        """
        coords = []
        for v in vertices:
            coords.extend([(v.end.x, v.end.y), (v.start.x, v.start.y)])
        if coords:
            pygame.draw.polygon(self.screen, color, coords, 0)

    def project(self, point: Point3D, scale: float, 
                abs_x: Optional[float] = None, 
                abs_y: Optional[float] = None) -> Point2D:
        """
        Project a 3D point onto the 2D screen using perspective projection.

        Args:
            point: 3D point to project
            scale: Scale factor for the projection
            abs_x: Optional x-offset (defaults to screen center)
            abs_y: Optional y-offset (defaults to screen center)

        Returns:
            Point2D: Projected 2D point
        """
        abs_y = self.window_height/2 if abs_y is None else abs_y
        abs_x = self.window_width/2 if abs_x is None else abs_x
        
        z_factor = self.FOV + point.z
        return Point2D(
            abs_x + (self.FOV * point.x) / z_factor * scale,
            abs_y + (self.FOV * point.y) / z_factor * scale
        )

    def draw_object(self, obj_index: int) -> bool:
        """Draw a single object from the objects list."""
        if 0 <= obj_index < len(self.objects):
            obj = self.objects[obj_index]
            
            # Draw filled faces first if enabled
            if obj.is_filled:
                faces = sorted(obj.faces, 
                             key=lambda face: face.get_center().z,
                             reverse=True)
                
                for face in faces:
                    points_2d = [self.project(point, obj.scale) for point in face.points]
                    polygon_points = [(p.x, p.y) for p in points_2d]
                    
                    if len(polygon_points) >= 3:
                        z_depth = min(1.0, max(0.3, 
                            (self.FOV + face.get_center().z) / (self.FOV * 2)))
                        
                        if isinstance(obj.color, str):
                            base_color = pygame.Color(obj.color)
                        else:
                            base_color = obj.color
                        
                        shaded_color = (
                            int(base_color[0] * z_depth),
                            int(base_color[1] * z_depth),
                            int(base_color[2] * z_depth)
                        )
                        
                        pygame.draw.polygon(self.screen, shaded_color, polygon_points)
            
            # Draw edges
            for vertex in obj.vertexArr:
                points = vertex.getPoints()
                projected_vertex = Vertex(
                    self.project(points[0], obj.scale),
                    self.project(points[1], obj.scale)
                )
                self.draw_2d(projected_vertex, obj.color)
            return True
        print(f"Error in draw_object: object at index {obj_index} does not exist")
        return False

    def draw_all(self) -> None:
        """Draw all objects in the renderer."""
        for i in range(len(self.objects)):
            self.draw_object(i)

    def _get_face_center(self, points: List[Point3D]) -> float:
        """Calculate average Z coordinate for depth sorting."""
        return sum(p.z for p in points) / len(points)

    def _get_object_faces(self, obj: Object3D) -> List[List[Point3D]]:
        """Extract faces from object's vertex array."""
        obj.update()  # Update object's connections
        faces = []
        used_connections = set()

        for point_set in obj.connects:
            if len(point_set) < 3:  # Skip if not enough points for a face
                continue
                
            for i in range(len(point_set)):
                for j in range(i + 1, len(point_set)):
                    for k in range(j + 1, len(point_set)):
                        # Create a unique key for this face
                        face_key = tuple(sorted([
                            tuple(point_set[i].getPointStart().toArray()),
                            tuple(point_set[j].getPointStart().toArray()),
                            tuple(point_set[k].getPointStart().toArray())
                        ]))
                        
                        if face_key not in used_connections:
                            faces.append([
                                point_set[i].getPointStart(),
                                point_set[j].getPointStart(),
                                point_set[k].getPointStart()
                            ])
                            used_connections.add(face_key)

        return faces

    def fill_object(self, obj_index: int) -> bool:
        """Fill a 3D object with solid faces."""
        if not (0 <= obj_index < len(self.objects)):
            print(f"Error in fill_object: object at index {obj_index} does not exist")
            return False

        obj = self.objects[obj_index]
        
        # Sort faces by Z depth (painter's algorithm)
        faces = sorted(obj.faces, 
                      key=lambda face: face.get_center().z,
                      reverse=True)

        # Draw each face
        for face in faces:
            # Project each point of the face to 2D
            points_2d = [self.project(point, obj.scale) for point in face.points]
            polygon_points = [(p.x, p.y) for p in points_2d]
            
            if len(polygon_points) >= 3:
                # Calculate shading based on face center Z
                z_depth = min(1.0, max(0.3, 
                    (self.FOV + face.get_center().z) / (self.FOV * 2)))
                
                if isinstance(obj.color, str):
                    base_color = pygame.Color(obj.color)
                else:
                    base_color = obj.color
                    
                shaded_color = (
                    int(base_color[0] * z_depth),
                    int(base_color[1] * z_depth),
                    int(base_color[2] * z_depth)
                )
                
                pygame.draw.polygon(self.screen, shaded_color, polygon_points)
                pygame.draw.polygon(self.screen, obj.color, polygon_points, 1)

        return True
