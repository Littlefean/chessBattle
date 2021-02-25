from player import *


class Game:
    def __init__(self, board, *args: Player):
        self.players = args
        self.board = board
        self.step = 0

    def isEnd(self):
        """判断五子棋棋局是否结束"""
        for player in self.players:
            # 遍历每一个玩家
            colorType = player.pieceKind.color
            positionList = self.board.getKindSet(colorType)
            for pieceLoc in positionList:
                # 遍历每一个棋子
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if [x, y] != [0, 0]:
                            fivePieces = [pieceLoc]
                            # 遍历棋子的每个方向
                            five = 0  # 正确的棋子数
                            pieceL = Position(pieceLoc.x, pieceLoc.y)
                            for i in range(4):
                                pieceL.x += x
                                pieceL.y += y
                                if self.board.isLocIn(pieceL):
                                    fivePieces.append(pieceL)
                                    if self.board.getPiece(pieceL).color == player.pieceKind.color:
                                        five += 1
                                else:
                                    break
                            if five == 4:
                                return player
        return None

    def play(self):
        """
        让对局实例进行一场对局
        直到对局结束
        返回赢得胜利的玩家对象
        若无玩家胜利，棋盘无法再下下去了，则返回None
        :return:
        """
        while True:
            for player in self.players:
                player.strategy()
                self.step += 1
                winner = self.isEnd()
                if winner is not None:
                    winner.score += 1
                    self.clear()
                    return winner
                if player.board.isFull():
                    self.clear()
                    return None

    def clear(self):
        """棋局清空"""
        self.board.clear()
        self.step = 0

    def __str__(self):
        print(f"当前棋局进行了{self.step}步")
        return ""
