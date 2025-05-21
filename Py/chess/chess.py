import pygame 

#constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
working_directory = "Py/chess/"
screen = pygame.display.set_mode((600, 600))

pygame.init()



class Pice:
    """Class representing a chess piece."""
    WHITE_ROOK = working_directory+"pieces-png/white-rook.png"
    WHITE_KNIGHT = working_directory+"pieces-png/white-knight.png"
    WHITE_BISHOP = working_directory+"pieces-png/white-bishop.png"
    WHITE_QUEEN = working_directory+"pieces-png/white-queen.png"
    WHITE_KING = working_directory+"pieces-png/white-king.png"
    WHITE_PAWN = working_directory+"pieces-png/white-pawn.png"
    BLACK_ROOK = working_directory+"pieces-png/black-rook.png"
    BLACK_KNIGHT = working_directory+"pieces-png/black-knight.png"
    BLACK_BISHOP = working_directory+"pieces-png/black-bishop.png"
    BLACK_QUEEN = working_directory+"pieces-png/black-queen.png"
    BLACK_KING = working_directory+"pieces-png/black-king.png"
    BLACK_PAWN = working_directory+"pieces-png/black-pawn.png"



    def __init__(self, color, type, x, y):
        self.color = color
        self.type = type
        self.x = x
        self.y = y

    def draw(self):
        """Draws the piece on the board."""
        piece_image = pygame.image.load(self.type)
        piece_image = pygame.transform.scale(piece_image, (75, 75))
        screen.blit(piece_image, (self.x * 75, self.y * 75))

        


class Board:
    """Class representing the chess board."""
    def __init__(self):
        self.pieces = []
        #self.create_board()
        #self.create_pieces()

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

    def draw_pieces(self):
        """Draws the pieces on the board."""
        for piece in self.pieces:
            piece.draw()

    def add_piece(self, piece):
        """Adds a piece to the board."""
        self.pieces.append(piece)


if __name__ == "__main__":
    board = Board()

    pygame.display.set_caption("Chess Game")
    board.add_piece(Pice(Pice.WHITE_PAWN, Pice.WHITE_PAWN, 0, 1))
    board.add_piece(Pice(Pice.WHITE_PAWN, Pice.WHITE_PAWN, 1, 1))
    board.add_piece(Pice(Pice.WHITE_PAWN, Pice.WHITE_PAWN, 2, 1))

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