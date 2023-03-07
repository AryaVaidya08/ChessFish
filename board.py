from colorama import Fore
import pieces
import math


# Alr I got some suggestions: 1. Instead of making a separate piece class, we should just go with the board holding
# the letters that represent each piece. I also wouldn't make separate classes for each type because that clutters
# memory. ~ Saraansh

# Arya Vaidya ~ 3/4/23 4:24 AM ~ Created the movesets for pawn, lateral, vertical, diagonal movement,
# made a GitHub, connected this replit to the GitHub, made the interactable game with input and
# everything, nothing relies on the board variable now (everything gets its data from the actual pieces),
# im tired as hell, please kill me, and im going to commit suicide
# Pinned and Checks work

# I think the github is broken :P

class Board:
    board = [["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""],
             ["", "", "", "", "", "", "", ""]]

    def __init__(self):
        self.wRook1 = pieces.Rook("a1", 1)
        self.wKnight1 = pieces.Knight("b1", 1)
        self.wBishop1 = pieces.Bishop("c1", 1)
        self.wQueen = pieces.Queen("d1", 1)
        self.wKing = pieces.King("e1", 1) #e3
        self.wBishop2 = pieces.Bishop("f1", 1)
        self.wKnight2 = pieces.Knight("g1", 1)
        self.wRook2 = pieces.Rook("h1", 1)
        self.wPawnA = pieces.Pawn("a2", 1)
        self.wPawnB = pieces.Pawn("b2", 1)
        self.wPawnC = pieces.Pawn("c2", 1)
        self.wPawnD = pieces.Pawn("d2", 1)
        self.wPawnE = pieces.Pawn("e2", 1)
        self.wPawnF = pieces.Pawn("f2", 1)
        self.wPawnG = pieces.Pawn("g2", 1)
        self.wPawnH = pieces.Pawn("h2", 1)

        self.bRook1 = pieces.Rook("a8", 2) #e6
        self.bKnight1 = pieces.Knight("b8", 2) #e5
        self.bBishop1 = pieces.Bishop("c8", 2)
        self.bQueen = pieces.Queen("d8", 2)
        self.bKing = pieces.King("e8", 2)
        self.bBishop2 = pieces.Bishop("f8", 2)
        self.bKnight2 = pieces.Knight("g8", 2)
        self.bRook2 = pieces.Rook("h8", 2)
        self.bPawnA = pieces.Pawn("a7", 2)
        self.bPawnB = pieces.Pawn("b7", 2)
        self.bPawnC = pieces.Pawn("c7", 2)
        self.bPawnD = pieces.Pawn("d7", 2)
        self.bPawnE = pieces.Pawn("e7", 2)
        self.bPawnF = pieces.Pawn("f7", 2)
        self.bPawnG = pieces.Pawn("g7", 2)
        self.bPawnH = pieces.Pawn("h7", 2)

        self.whitePieces = [
            self.wRook1, self.wKnight1, self.wBishop1, self.wQueen, self.wKing,
            self.wBishop2, self.wKnight2, self.wRook2, self.wPawnA, self.wPawnB,
            self.wPawnC, self.wPawnD, self.wPawnE, self.wPawnF, self.wPawnG,
            self.wPawnH
        ]
        self.blackPieces = [
            self.bRook1, self.bKnight1, self.bBishop1, self.bQueen, self.bKing,
            self.bBishop2, self.bKnight2, self.bRook2, self.bPawnA, self.bPawnB,
            self.bPawnC, self.bPawnD, self.bPawnE, self.bPawnF, self.bPawnG,
            self.bPawnH
        ]
        self.piecesList = [self.whitePieces, self.blackPieces]

    def printBoard(self):
        rankList = "87654321"
        fileList = "abcdefgh"

        piecesPos = []
        for whitePiece in self.whitePieces:
            piecesPos.append(whitePiece.position)
        for blackPiece in self.blackPieces:
            piecesPos.append(blackPiece.position)

        # Reset Board
        for rank in range(0, 8):
            for file in range(0, 8):
                self.board[rank][file] = ""

        # Add Pieces
        for colorList in self.piecesList:
            for piece in colorList:
                color = piece.color
                position = piece.position
                if position == "X0":
                    continue
                rankPos = rankList.index(position[1])
                filePos = fileList.index(position[0])
                self.board[rankPos][filePos] = piece.__str__()

        # Print Cooly
        print(Fore.LIGHTCYAN_EX + "\n\t------------------------")
        for rank in range(0, 8):
            print(Fore.LIGHTBLUE_EX + f"[{int(math.fabs(rank - 8))}]", end="\t")
            for file in range(0, 8):
                if self.board[rank][file] == "":
                    self.board[rank][file] = " "

                # ive definitely made this overcomplicated ~ Arya
                position = f"{fileList[file]}{rankList[rank]}"
                color = Fore.BLACK
                try:
                    index = piecesPos.index(position)
                    row = index // 16
                    col = index % 16
                    colorNum = self.piecesList[row][col].color
                    if colorNum == 1:
                        color = Fore.LIGHTWHITE_EX
                    elif colorNum == 2:
                        color = Fore.LIGHTBLACK_EX
                except ValueError:
                    color = Fore.LIGHTGREEN_EX

                print(f"{color}[{self.board[rank][file]}]", end="")
            print(Fore.LIGHTCYAN_EX + "\n\t------------------------")

        print(Fore.LIGHTBLUE_EX + "\n\t[a][b][c][d][e][f][g][h]\n\n")

    def move(self, start, end, color, test=False):

        if color == "white":
            for piece in self.whitePieces:
                if piece.position == start:
                    if not self.emptySquare(end):
                        if not test:
                            self.takePiece(end, color)
                    piece.position = end
                    break
        elif color == "black":
            for piece in self.blackPieces:
                if piece.position == start:
                    if not self.emptySquare(end):
                        if not test:
                            self.takePiece(end, color)
                    piece.position = end
                    break

    def pinned(self, start, end, color):
        pinned = False
        oppositeColor = ""
        if color == "white":
            oppositeColor = "black"
        else:
            oppositeColor = "white"
        self.move(start, end, color, True)
        if self.check(oppositeColor):
            pinned = True
        else:
            pinned = False
        self.move(end, start, color, True)
        return pinned

    def checkMove(self, start, end, color):  # checks if moves are legal
        #f2-f3
        startPosString = str(start[(len(start) - 2):])
        endPosString = str(end[(len(end) - 2):])
        legalMoves = []

        if color == "white":
            for piece in self.whitePieces:
                if startPosString == piece.position:  # Find the right piece
                    filePos = piece.position[0]  # d
                    rankPos = piece.position[1]  # 4
                    # Need to check for En Passant, Pinned Moves, Castles, etc
                    for move in piece.moveset:
                        if move == "p":
                            # One Square Ahead
                            if self.emptySquare(f"{filePos}{int(rankPos) + 1}"):
                                legalMoves.append(f"{filePos}{int(rankPos) + 1}")
                                # Two Squares Ahead
                                if rankPos == "2" and self.emptySquare(f"{filePos}{int(rankPos) + 2}"):
                                    legalMoves.append(f"{filePos}{int(rankPos) + 2}")

                            attackSquareLeft = f"{chr(ord(filePos) - 1)}{int(rankPos) + 1}"
                            attackSquareRight = f"{chr(ord(filePos) + 1)}{int(rankPos) + 1}"
                            if not self.emptySquare(attackSquareLeft) and self.getColorOfPiece(attackSquareLeft) == 2:
                                legalMoves.append(attackSquareLeft)
                            if not self.emptySquare(attackSquareRight) and self.getColorOfPiece(attackSquareRight) == 2:
                                legalMoves.append(attackSquareRight)
                        elif move == "l":
                            # Lateral Moves
                            # Left Moves
                            for file in range(ord(filePos) - 1, ord("a") - 1, -1):
                                testPos = f"{chr(file)}{rankPos}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break

                            # Right Moves
                            for file in range(ord(filePos) + 1, ord("h") + 1):
                                testPos = f"{chr(file)}{rankPos}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break
                        elif move == "v":
                            # Vertical Moves
                            # Down Moves
                            for rank in range(int(rankPos) - 1, 0, -1):
                                testPos = f"{filePos}{rank}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break

                            # Up Moves
                            for rank in range(int(rankPos) + 1, 8):
                                testPos = f"{filePos}{rank}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break
                        elif move == "d":
                            # Diagonal Moves
                            # Up Left (rank + n, file - n)
                            step = 1
                            while ord(filePos) - step >= ord("a") and int(rankPos) + step <= 8:
                                testPos = f"{chr(ord(filePos) - step)}{int(rankPos) + step}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                    step += 1
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break

                            # Up Right (rank + n, file + n)
                            step = 1
                            while ord(filePos) + step <= ord("h") and int(rankPos) + step <= 8:
                                testPos = f"{chr(ord(filePos) + step)}{int(rankPos) + step}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                    step += 1
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break

                            # Down Left (rank - n, file - n)
                            step = 1
                            while ord(filePos) - step >= ord("a") and int(rankPos) - step >= 1:
                                testPos = f"{chr(ord(filePos) - step)}{int(rankPos) - step}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                    step += 1
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break

                            # Down Right (rank - n, file + n)
                            step = 1
                            while ord(filePos) + step <= ord("h") and int(rankPos) - step >= 1:
                                testPos = f"{chr(ord(filePos) + step)}{int(rankPos) - step}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                    step += 1
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break
                        elif move == "g":
                            positions = [f"{chr(ord(filePos) - 1)}{int(rankPos) + 2}",  # Up 2 Left 1
                                         f"{chr(ord(filePos) + 1)}{int(rankPos) + 2}",  # Up 2 Right 1
                                         f"{chr(ord(filePos) + 2)}{int(rankPos) + 1}",  # Right 2 Up 1
                                         f"{chr(ord(filePos) + 2)}{int(rankPos) - 1}",  # Right 2 Down 1
                                         f"{chr(ord(filePos) - 1)}{int(rankPos) - 2}",  # Down 2 Left 1
                                         f"{chr(ord(filePos) + 1)}{int(rankPos) - 2}",  # Down 2 Right 1
                                         f"{chr(ord(filePos) - 2)}{int(rankPos) + 1}",  # Left 2 Up 1
                                         f"{chr(ord(filePos) - 2)}{int(rankPos) - 1}"]  # Left 2 Down 1

                            for position in positions:
                                if self.squareExists(position):
                                    if self.emptySquare(position) or (
                                            not self.emptySquare(position) and self.getColorOfPiece(position) == 2):
                                        legalMoves.append(position)
                        elif move == "k":
                            positions = [f"{chr(ord(filePos) + 1)}{rankPos}",  # Right
                                         f"{chr(ord(filePos) + 1)}{int(rankPos) + 1}",  # Up Right
                                         f"{filePos}{int(rankPos) + 1}",  # Up
                                         f"{chr(ord(filePos) - 1)}{int(rankPos) + 1}",  # Up Left
                                         f"{chr(ord(filePos) - 1)}{rankPos}",  # Left
                                         f"{chr(ord(filePos) - 1)}{int(rankPos) - 1}",  # Down Left
                                         f"{filePos}{int(rankPos) - 1}",  # Down
                                         f"{chr(ord(filePos) + 1)}{int(rankPos) - 1}"]  # Down Right

                            for position in positions:
                                if self.emptySquare(position):
                                    legalMoves.append(position)
                                else:
                                    if self.getColorOfPiece(position) == 2:
                                        legalMoves.append(position)
        elif color == "black":
            for piece in self.blackPieces:
                if startPosString == piece.position:  # Find the right piece
                    filePos = piece.position[0]
                    rankPos = piece.position[1]

                    for move in piece.moveset:
                        if move == "p":
                            # One Square Ahead
                            if self.emptySquare(f"{filePos}{int(rankPos) - 1}"):
                                legalMoves.append(f"{filePos}{int(rankPos) - 1}")
                                # Two Squares Ahead
                                if rankPos == "7" and self.emptySquare(f"{filePos}{int(rankPos) - 2}"):
                                    legalMoves.append(f"{filePos}{int(rankPos) - 2}")
                            attackSquareLeft = f"{chr(ord(filePos) - 1)}{int(rankPos) - 1}"
                            attackSquareRight = f"{chr(ord(filePos) + 1)}{int(rankPos) - 1}"
                            if not self.emptySquare(attackSquareLeft) and self.getColorOfPiece(attackSquareLeft) == 1:
                                legalMoves.append(attackSquareLeft)
                            if not self.emptySquare(attackSquareRight) and self.getColorOfPiece(attackSquareRight) == 1:
                                legalMoves.append(attackSquareRight)
                        elif move == "l":
                            # Lateral Moves
                            # Left Moves
                            for file in range(ord(filePos) - 1, ord("a") - 1, -1):
                                testPos = f"{chr(file)}{rankPos}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break

                            # Right Moves
                            for file in range(ord(filePos) + 1, ord("h") + 1):
                                testPos = f"{chr(file)}{rankPos}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break
                        elif move == "v":
                            # Vertical Moves
                            # Down Moves
                            for rank in range(int(rankPos) + 1, 8):
                                testPos = f"{filePos}{rank}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break

                            # Up Moves
                            for rank in range(int(rankPos) - 1, 0, -1):
                                testPos = f"{filePos}{rank}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break
                        elif move == "d":
                            # Diagonal Moves
                            # Up Left (rank - n, file + n)
                            step = 1
                            while ord(filePos) + step <= ord("h") and int(rankPos) - step >= 1:
                                testPos = f"{chr(ord(filePos) + step)}{int(rankPos) - step}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                    step += 1
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break

                            # Up Right (rank - n, file - n)
                            step = 1
                            while ord(filePos) - step >= ord("a") and int(rankPos) - step >= 1:
                                testPos = f"{chr(ord(filePos) - step)}{int(rankPos) - step}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                    step += 1
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break

                            # Down Left (rank + n, file + n)
                            step = 1
                            while ord(filePos) + step <= ord("h") and int(rankPos) + step <= 8:
                                testPos = f"{chr(ord(filePos) + step)}{int(rankPos) + step}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                    step += 1
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break

                            # Down Right (rank + n, file - n)
                            step = 1

                            while ord(filePos) - step >= ord("a") and int(rankPos) + step <= 8:
                                testPos = f"{chr(ord(filePos) - step)}{int(rankPos) + step}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                    step += 1
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break
                        elif move == "g":
                            positions = [f"{chr(ord(filePos) - 1)}{int(rankPos) + 2}",
                                         f"{chr(ord(filePos) + 1)}{int(rankPos) + 2}",
                                         f"{chr(ord(filePos) + 2)}{int(rankPos) + 1}",
                                         f"{chr(ord(filePos) + 2)}{int(rankPos) - 1}",
                                         f"{chr(ord(filePos) - 1)}{int(rankPos) - 2}",
                                         f"{chr(ord(filePos) + 1)}{int(rankPos) - 2}",
                                         f"{chr(ord(filePos) - 2)}{int(rankPos) + 1}",
                                         f"{chr(ord(filePos) - 2)}{int(rankPos) - 1}"]

                            for position in positions:
                                if self.squareExists(position):
                                    if self.emptySquare(position) or (
                                            not self.emptySquare(position) and self.getColorOfPiece(position) == 1):
                                        legalMoves.append(position)
                        elif move == "k":
                            positions = [f"{chr(ord(filePos) + 1)}{rankPos}",  # Left
                                         f"{chr(ord(filePos) + 1)}{int(rankPos) + 1}",  # Down Left
                                         f"{filePos}{int(rankPos) + 1}",  # Down
                                         f"{chr(ord(filePos) - 1)}{int(rankPos) + 1}",  # Down Right
                                         f"{chr(ord(filePos) - 1)}{rankPos}",  # Right
                                         f"{chr(ord(filePos) - 1)}{int(rankPos) - 1}",  # Up Right
                                         f"{filePos}{int(rankPos) - 1}",  # Up
                                         f"{chr(ord(filePos) + 1)}{int(rankPos) - 1}"]  # Up Right

                            for position in positions:
                                if self.emptySquare(position):
                                    legalMoves.append(position)
                                else:
                                    if self.getColorOfPiece(position) == 1:
                                        legalMoves.append(position)

        legalMoves = set(legalMoves)

        if not endPosString == "XX":
            inLegal = endPosString in legalMoves
            isPinned = False
            if inLegal:
                isPinned = self.pinned(start, end, color)
                if isPinned:
                    return False
                else:
                    return True
            else:
                return False
        else:
            actualLegalMoves = []
            for move in legalMoves:
                if self.squareExists(move):
                    isPinned = self.pinned(start, move, color)
                    if not isPinned:
                        actualLegalMoves.append(move)
            return actualLegalMoves

    def squareExists(self, position):
        fileList = "abcdefgh"
        rankList = "12345678"
        file = position[0]
        rank = position[1:]
        try:
            fileList.index(file)
            rankList.index(rank)
            return True
        except ValueError:
            return False

    def checkPieceExists(self, turn, start):
        if turn == "white":
            for piece in self.whitePieces:
                if piece.position == start:
                    return True
        if turn == "black":
            for piece in self.blackPieces:
                if piece.position == start:
                    return True
        return False

    def emptySquare(self, position):
        for list in self.piecesList:
            for piece in list:
                if piece.position == position:
                    return False
        return True

    def getColorOfPiece(self, position):
        for list in self.piecesList:
            for piece in list:
                if piece.position == position:
                    return piece.color

    def check(self, color):
        if color == "white":
            # Get Black King Position
            blackKingPos = ""
            for piece in self.blackPieces:
                if piece.__str__() == "k":
                    blackKingPos = piece.position
                    break
            #print(blackKingPos)
            for piece in self.whitePieces:
                if self.checkMove(piece.position, blackKingPos, "white"):
                    return True
            return False
        elif color == "black":
            # Get White King Position
            whiteKingPos = ""
            for piece in self.whitePieces:
                if piece.__str__() == "k":
                    whiteKingPos = piece.position
                    break
            #print(whiteKingPos)
            for piece in self.blackPieces:
                if self.checkMove(piece.position, whiteKingPos, "black"):
                    return True
            return False

    def checkMate(self, color):
        legalMoves = []
        # Get Legal Moves
        if color == "white":
            #Check if white is able to mate the black king
            for piece in self.blackPieces:
                moves = self.checkMove(piece.position, "XX", "black")
                for move in moves:
                    legalMoves.append(move)
        elif color == "black":
            for piece in self.whitePieces:
                moves = self.checkMove(piece.position, "XX", "white")
                for move in moves:
                    legalMoves.append(move)
        if len(legalMoves) == 0:
            # Check For Stalemate
            return True
        else:
            return False

    def takePiece(self, position, color):
        if color == "white":
            for piece in self.blackPieces:
                if piece.position == position:
                    piece.position = "X0"
                    break
        elif color == "black":
            for piece in self.whitePieces:
                if piece.position == position:
                    piece.position = "X0"
                    break
