from const import *
from square import Square
from piece import *

class Board:
    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)]  # creates a 2D list of 8x8
        self._create()
        self._add_pieces()

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self):
        ## place pawns for black and then white
        for row in (1, 6):
            color = 'black' if row == 1 else 'white'
            for col in range(COLS):
                self.squares[row][col] = Square(row, col, Pawn(color))
        
        ## place the back row for black and then white
        for row in (0,7):
            color = 'black' if row == 0 else 'white'
            for col in range(COLS):
                if col == 0 or col == 7:
                    self.squares[row][col] = Square(row, col, Rook(color))
                elif col == 1 or col == 6:
                    self.squares[row][col] = Square(row, col, Knight(color))
                elif col == 2 or col == 5:
                    self.squares[row][col] = Square(row, col, Bishop(color))
                elif col == 3:
                    self.squares[row][col] = Square(row, col, Queen(color))
                else:
                    self.squares[row][col] = Square(row, col, King(color))