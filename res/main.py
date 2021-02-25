"""
下棋游戏
2021.2.23
by littlefean
"""
from game import *


def main():
    board = Board.getInstance()
    ai1 = Player("a1", board, Piece.whiteInstance())
    ai2 = Player("a2", board, Piece.blackInstance())
    # 进行n场比赛
    game = Game(board, ai1, ai2)
    for i in range(100):
        game.play()
    print(f"{ai1.name}: {ai1.score}\n{ai2.name}: {ai2.score}")
    print(f"{ai1.score / ai2.score}")
    pass


if __name__ == '__main__':
    main()
