import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

global display


def drawRects(rects: list):
    global display
    rectWith = (WINDOW_WIDTH - 100) / rects.__len__()
    X = 100
    for rectHight in rects:
        X += rectWith
        rect = pygame.Rect((X, WINDOW_HEIGHT - 100 - rectHight), (rectWith, rectHight))
        pygame.draw.rect(display, "Green", rect)


def main():
    """Main program entry point."""
    global display
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    running = True
    display.fill((0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        drawRects([100, 200, 69, 420, 2000, 10, 20, 1, 33, 15])
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
