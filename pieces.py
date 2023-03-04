# p ~ goofy ass pawn moves
# d ~ diagonal
# l ~ lateral
# v ~ vertical
# g ~ goofy ass knight moves
# k ~ goofy ass king moves

class Piece:

    def __init__(self, position, color):
        self.position = position
        self.color = color

class Pawn(Piece):
    moveset = "p"
    moveLength = 1

    def __str__(self):
        return "p"

class Rook(Piece):
    moveset = "vl"
    moveLength = 7

    def __str__(self):
        return "r"

class Knight(Piece):
    moveset = "g"
    moveLength = 7

    def __str__(self):
        return "n"

class Bishop(Piece):
    moveset = "d"
    moveLength = 7

    def __str__(self):
        return "b"

class Queen(Piece):
    moveset = "vld"
    moveLength = 7

    def __str__(self):
        return "q"

class King(Piece):
    moveset = "k"
    moveLength = 1

    def __str__(self):
        return "k"
