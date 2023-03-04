from colorama import Fore
import pieces

# Alr I got some suggestions: 1. Instead of making a separate piece class, we should just go with the board holding
# the letters that represent each piece. I also wouldn't make separate classes for each type because that clutters
# memory. ~ Saraansh

# Arya Vaidya ~ 3/4/23 3:16 AM ~ Created the movesets for pawn, lateral, and vertical movement,
# made a GitHub, connected this replit to the GitHub, made the interactable game with input and
# everything, nothing relies on the board variable now (everything gets its data from the actual pieces),
# im tired as hell, please kill me, and im going to commit suicide

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
        self.wKing = pieces.King("e1", 1)
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

        self.bRook1 = pieces.Rook("a8", 2)
        self.bKnight1 = pieces.Knight("b8", 2)
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
                rankPos = rankList.index(position[1])
                filePos = fileList.index(position[0])
                self.board[rankPos][filePos] = piece.__str__()

        # Print Cooly

        print(Fore.LIGHTCYAN_EX + "\n------------------------")
        for rank in range(0, 8):
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
            print(Fore.LIGHTCYAN_EX + "\n------------------------")

    def move(self, start, end, color):

        if color == "white":
            for piece in self.whitePieces:
                if piece.position == start:
                    piece.position = end
                    break
        elif color == "black":
            for piece in self.blackPieces:
                if piece.position == start:
                    piece.position = end
                    break

    def checkMove(self, start, end, color):  # checks if moves are legal

        startPosString = str(start[(len(start) - 2):])
        endPosString = str(end[(len(end) - 2):])
        legalMoves = []

        if color == "white":
            for piece in self.whitePieces:
                if startPosString == piece.position:  # Find the right piece
                    filePos = piece.position[0]
                    rankPos = piece.position[1]

                    for move in piece.moveset:
                        if move == "p":
                            #One Square Ahead
                            if self.emptySquare(f"{filePos}{int(rankPos) + 1}"):
                                legalMoves.append(f"{filePos}{int(rankPos) + 1}")
                                #Two Squares Ahead
                                if rankPos == "2" and self.emptySquare(f"{filePos}{int(rankPos) + 2}"):
                                    legalMoves.append(f"{filePos}{int(rankPos) + 2}")

                            attackSquareLeft = f"{chr(ord(filePos) - 1)}{int(rankPos) + 1}"
                            attackSquareRight = f"{chr(ord(filePos) + 1)}{int(rankPos) + 1}"
                            if not self.emptySquare(attackSquareLeft) and self.getColorOfPiece(attackSquareLeft) == 2:
                                legalMoves.append(attackSquareLeft)
                            if not self.emptySquare(attackSquareRight) and self.getColorOfPiece(attackSquareRight) == 2:
                                legalMoves.append(attackSquareRight)
                        elif move == "l":
                            #Lateral Moves
                            #Left Moves
                            for file in range(ord(filePos) - 1, ord("a") - 1, -1):
                                testPos = f"{chr(file)}{rankPos}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break

                            #Right Moves
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
                            #Down Moves
                            for rank in range(int(rankPos) - 1, 0, -1):
                                testPos = f"{filePos}{rank}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 2:
                                        legalMoves.append(testPos)
                                    break

                            #Up Moves
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
                            pass
                        elif move == "g":
                            # Knight Moves
                            pass
                        elif move == "k":
                            # King Moves
                            pass
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
                            #Left Moves
                            for file in range(ord(filePos) - 1, ord("a") - 1, -1):
                                testPos = f"{chr(file)}{rankPos}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break

                            #Right Moves
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
                            #Down Moves
                            for rank in range(int(rankPos) + 1, 8):
                                testPos = f"{filePos}{rank}"
                                if self.emptySquare(testPos):
                                    legalMoves.append(testPos)
                                else:
                                    if self.getColorOfPiece(testPos) == 1:
                                        legalMoves.append(testPos)
                                    break

                            #Up Moves
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
                            pass
                        elif move == "g":
                            # Knight Moves
                            pass
                        elif move == "k":
                            # King Moves
                            pass

        legalMoves = set(legalMoves)
        print(legalMoves)
        return endPosString in legalMoves

    def checkPieceExists(self, turn, start):
        if turn == "white":
            for piece in self.whitePieces:
                if piece.position == start:
                    return True
        elif turn == "black":
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
    def checkMate(self):
        # Do a checkmate check
        return False
