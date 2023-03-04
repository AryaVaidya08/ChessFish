import board
from colorama import Fore


class Game:

    def __init__(self):
        self.chessBoard = board.Board()
        self.chessBoard.printBoard()

    def startGame(self):
        moveNumber = 1

        while True:
            firstCheck = True

            whitePos = input(Fore.WHITE + f"Move #{moveNumber}. White's Move. Enter the starting square and end square seperated by a dash (Ex: a2-a4): ")
            while True:
                if not firstCheck:
                    whitePos = input(Fore.WHITE + "Input Error. Enter the starting square and end square seperated by a dash (Ex: a2-a4): ")
                firstCheck = False
                if len(whitePos) != 5:
                    continue
                if not self.chessBoard.checkPieceExists("white", whitePos[:2]):
                    continue
                if not self.chessBoard.checkMove(whitePos[:2], whitePos[3:], "white"):
                    continue
                break

            self.chessBoard.move(whitePos[:2], whitePos[3:], "white")
            if self.chessBoard.checkMate():
                print(Fore.WHITE + "White won!")
                break

            self.chessBoard.printBoard()

            firstCheck = True
            blackPos = input(Fore.WHITE + f"Move #{moveNumber}. Black's Move. Enter the starting square and end square seperated by a dash (Ex: a2-a4): ")
            while True:
                if not firstCheck:
                    blackPos = input(Fore.WHITE + "Input Error. Enter the starting square and end square seperated by a dash (Ex: a2-a4): ")
                firstCheck = False
                if len(blackPos) != 5:
                    continue
                if not self.chessBoard.checkPieceExists("black", blackPos[:2]):
                    continue
                if not self.chessBoard.checkMove(blackPos[:2], blackPos[3:], "black"):
                    continue
                break
            self.chessBoard.move(blackPos[:2], blackPos[3:], "black")
            if self.chessBoard.checkMate():
                print(Fore.WHITE + "Black Won!")
                break

            self.chessBoard.printBoard()
            moveNumber += 1
