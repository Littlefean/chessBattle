"""
此模块存放构建棋类游戏所需要的基础类
"""


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"<{self.x}, {self.y}>"


class Piece:
    WHITE_COLOR = (255, 255, 255)
    BLACK_COLOR = (0, 0, 0)
    NULL_COLOR = (222, 156, 0)

    def __init__(self, color):
        self.color = color
        # self.host = host

    @staticmethod
    def whiteInstance():
        return Piece(Piece.WHITE_COLOR)

    @staticmethod
    def blackInstance():
        return Piece(Piece.BLACK_COLOR)

    @staticmethod
    def nullPiece():
        return Piece(Piece.NULL_COLOR)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__arr = []
        for y in range(height):
            line = []
            for x in range(height):
                line.append(Piece.nullPiece())
            self.__arr.append(line)

    def clear(self):
        """初始化棋盘"""
        self.__arr = []
        for y in range(self.height):
            line = []
            for x in range(self.height):
                line.append(Piece.nullPiece())
            self.__arr.append(line)

    def getPiece(self, p: Position):
        """返回某位置的棋子"""
        return self.__arr[p.y][p.x]

    def putPiece(self, p: Position, piece):
        """强行修改"""
        self.__arr[p.y][p.x] = piece

    def isLocIn(self, p: Position):
        """判断一个坐标是否在棋盘上"""
        return p.x in range(self.width) and p.y in range(self.height)

    def isNull(self, p: Position):
        """判断一个坐标上是否是空位置"""
        return self.getPiece(p).color == Piece.NULL_COLOR

    def getNullSet(self):
        """获取所有空位置的坐标"""
        nullSet = []
        for y in range(self.height):
            for x in range(self.width):
                if self.__arr[y][x].color == Piece.NULL_COLOR:
                    nullSet.append(Position(x, y))
        return nullSet

    def isFull(self):
        """棋盘是不是没有空位置了"""
        return len(self.getNullSet()) == 0

    def getKindSet(self, color):
        """获取一类棋子的所有位置坐标"""
        pieceSet = []
        for y in range(self.height):
            for x in range(self.width):
                if self.__arr[y][x].color == color:
                    pieceSet.append(Position(x, y))
        return pieceSet

    def __str__(self):
        pieceChar = {
            Piece.NULL_COLOR: " ",
            Piece.BLACK_COLOR: "X",
            Piece.WHITE_COLOR: "O",
        }
        print("__" * self.width)
        for line in self.__arr:
            for item in line:
                assert type(item) == Piece
                c = item.color
                print(pieceChar[c], end=" ")
            print()
        print("__" * self.width)
        return ""

    @staticmethod
    def getInstance():
        return Board(19, 19)
