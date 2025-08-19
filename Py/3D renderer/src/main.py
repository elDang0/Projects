import pygame as pyg
from Renderer import Renderer3D
from object import Object3D, StdObjects

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

def main():
    """Main program entry point."""
    pyg.init()
    clock = pyg.time.Clock()
    display = pyg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    # Create renderer and add cube
    renderer = Renderer3D(WINDOW_WIDTH, WINDOW_HEIGHT, display)
    cube = StdObjects.cube()  # Changed: use factory method directly
    renderer.add_object(cube)

    # Main game loop
    running = True
    while running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                running = False

        display.fill((0, 0, 0))
        renderer.draw_all()
        pyg.display.flip()
        clock.tick(FPS)

    pyg.quit()

if __name__ == "__main__":
    main()