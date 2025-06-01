import pygame
from pices import *


# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
working_directory = "Py/chess/"
screen = pygame.display.set_mode((600, 600))

pygame.init()


class Drawer:
    """that draws the chess board and pieces."""

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    WHITE_ROOK = working_directory + "pieces-png/white-rook.png"
    WHITE_KNIGHT = working_directory + "pieces-png/white-knight.png"
    WHITE_BISHOP = working_directory + "pieces-png/white-bishop.png"
    WHITE_QUEEN = working_directory + "pieces-png/white-queen.png"
    WHITE_KING = working_directory + "pieces-png/white-king.png"
    WHITE_PAWN = working_directory + "pieces-png/white-pawn.png"
    BLACK_ROOK = working_directory + "pieces-png/black-rook.png"
    BLACK_KNIGHT = working_directory + "pieces-png/black-knight.png"
    BLACK_BISHOP = working_directory + "pieces-png/black-bishop.png"
    BLACK_QUEEN = working_directory + "pieces-png/black-queen.png"
    BLACK_KING = working_directory + "pieces-png/black-king.png"
    BLACK_PAWN = working_directory + "pieces-png/black-pawn.png"

    def drawPiece(self, piece):
        """Draws the piece on the board."""
        piece_image = pygame.image.load(piece.type)
        piece_image = pygame.transform.scale(piece_image, (75, 75))
        screen.blit(piece_image, (piece.x * 75, piece.y * 75))

    def draw_board(self):
        """Draws the chess board on the screen."""
        screen.fill(RED)
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    color = BLACK
                else:
                    color = WHITE
                pygame.draw.rect(screen, color, (col * 75, row * 75, 75, 75))


if __name__ == "__main__":
    board = Board()

    pygame.display.set_caption("Chess Game")
    board.crate_board()
    board.crate_pieces()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill(WHITE)
        board.draw_board()
        for piece in board.pieces:
            piece.draw()
        pygame.display.flip()
