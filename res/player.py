"""
此模块存放玩家类的策略代码
"""
import random
from basic import *


class Player:
    def __init__(self, name, board, piece):
        self.name = name
        self.board = board
        self.pieceKind = piece
        self.score = 0
        self.strategy = self.randPutPiece2  # 当前使用的策略函数

    def __putPiece(self, p):
        """在棋盘上下一个棋子，请先自觉保证此方法只能在自己回合中执行一次"""
        piece = self.board.getPiece(p)
        if piece.color == Piece.NULL_COLOR:
            self.board.putPiece(p, self.pieceKind)
        return piece.color == Piece.NULL_COLOR

    def __getRound(self, p):
        """获取一个坐标周围一圈坐标并以列表返回，不含棋盘之外的坐标"""
        left = max(0, p.x - 1)
        right = min(self.board.width - 1, p.x + 1)
        top = max(0, p.y - 1)
        bottom = min(self.board.height - 1, p.y + 1)
        locArr = []
        for y in range(top, bottom + 1):
            for x in range(left, right + 1):
                if [x, y] != [p.x, p.y]:
                    locArr.append(Position(x, y))
        return locArr

    def randPutPiece(self):
        """
        随机下棋的策略
        获得一个棋盘里的所有空位置，随机挑一个空位置下
        :return:
        """
        s = self.board.getNullSet()
        if not self.board.isFull():
            p = random.choice(s)
            self.__putPiece(p)

    def randPutPiece1(self):
        """
        在自己下过棋的旁边的空位置上下一个棋
        这种挑选是有顺序的，优先选左上角的空位，最后选右下角的空位
        若自己没下过，或者没有上述符合条件的位置，则随机挑一个空位置下
        :return:
        """
        selfArr = self.board.getKindSet(self.pieceKind.color)
        # 棋盘没满
        if not self.board.isFull():
            # 自己还没下过
            if len(selfArr) == 0:
                self.randPutPiece()
            # 自己下过
            else:
                # 遍历自己的每一个位置
                for selfPiece in selfArr:
                    selfRound = self.__getRound(selfPiece)
                    # 遍历这一圈的每一个位置
                    for srLoc in selfRound:
                        # 如果是空位置
                        if self.board.isNull(srLoc):
                            # 下这里
                            self.__putPiece(srLoc)
                            return
                    # 如果这一圈没有空位置
                    else:
                        continue
                # 若都没空位置
                else:
                    self.randPutPiece()

    def randPutPiece2(self):
        """
        在自己下过棋的旁边的空位置上下一个棋
        这种挑选与1不同的是，它是随机选则的空位置，也是随机选择的自己的棋子
        若自己没下过，或者没有上述符合条件的位置，则随机挑一个空位置下
        :return:
        """
        selfArr = self.board.getKindSet(self.pieceKind.color)
        random.shuffle(selfArr)
        # 棋盘没满
        if not self.board.isFull():
            # 自己还没下过
            if len(selfArr) == 0:
                self.randPutPiece()
            # 自己下过
            else:
                # 遍历自己的每一个位置
                for selfPiece in selfArr:
                    selfRound = self.__getRound(selfPiece)
                    random.shuffle(selfRound)
                    # 遍历这一圈的每一个位置
                    for srLoc in selfRound:
                        # 如果是空位置
                        if self.board.isNull(srLoc):
                            # 下这里
                            self.__putPiece(srLoc)
                            return
                    # 如果这一圈没有空位置
                    else:
                        continue
                # 若都没空位置
                else:
                    self.randPutPiece()

    def strategy3(self):
        """
        策略3
        :return:
        """
        # 先检测对方最长的

        pass