class Square:
    def __init__(self, row, col, piece=None):  # <1>
        self.row = row
        self.col = col
        self.piece = piece

    def has_piece(self):
        return self.piece is not None