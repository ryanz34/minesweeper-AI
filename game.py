from random import choice
from copy import deepcopy

class MinesweeperGame:

    def __init__(self, xdim, ydim, bomb):
        self.xdim = xdim
        self.ydim = ydim
        self.bomb = bomb

        self.game_board = [[0] * xdim for _ in range(ydim)]
        self.hidden_board = [[True] * xdim for _ in range(ydim)]
        self.marked_board = [[False] * xdim for _ in range(ydim)]

    def generate_bombs(self):
        bomb_positions = []
        board_spots = [i for i in range(xdim * ydim)]

        for k in range(self.bomb):
            pos = choice(board_spots)

            bomb_positions.append(pos)
            board_spots.remove(pos)

        for i in bomb_positions:
            self.game_board[i // self.xdim][i % self.xdim] = 9

    def compute_neighbours(self):
        for y in range(self.ydim):
            for x in range(self.xdim):

                if self.game_board[y][x] != 9:
                    bomb_num = 0

                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= x + i < self.xdim and 0 <= y + j < self.ydim:
                                if self.game_board[y + j][x + i] == 9:
                                    bomb_num += 1

                    self.game_board[y][x] = bomb_num

    def reveal(self, x, y):
        visit = {(x, y)}
        to_visit = [(x, y)]
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while len(to_visit) != 0:
            position = to_visit.pop(0)

            self.hidden_board[position[1]][position[0]] = False

            if self.game_board[position[1]][position[0]] == 0:
                for d in direction:
                    if 0 <= position[0] + d[0] < self.xdim and 0 <= position[1] + d[1] < self.ydim:
                        p = (position[0] + d[0], position[1] + d[1])

                        if p not in visit:
                            to_visit.append(p)
                            visit.add(p)

        if self.game_board[y][x] == 9:
            return True

    def print_board(self):
        for y in range(self.ydim):
            for x in range(self.xdim):
                if self.marked_board[y][x]:
                    print("M", end="")
                elif self.hidden_board[y][x]:
                    print("*", end="")
                else:
                    print(self.game_board[y][x], end="")
            print()

    def win(self):
        for y in range(self.ydim):
            for x in range(self.xdim):
                if self.game_board[y][x] != 9 and self.hidden_board[y][x]:
                    return False
        return True

    def create_game(self):
        self.generate_bombs()
        self.compute_neighbours()

    def get_board(self):
        board = deepcopy(self.game_board)

        for y in range(self.ydim):
            for x in range(self.xdim):
                if self.marked_board[y][x]:
                    board[y][x] = -2
                elif self.hidden_board[y][x]:
                    board[y][x] = -1

        return board


xdim = int(input("X-dimension: "))
ydim = int(input("Y-dimension: "))
bomb = int(input("Number of bombs: "))

g = MinesweeperGame(xdim, ydim, bomb)
g.create_game()
g.print_board()
while True:
    x = int(input())
    y = int(input())

    o = g.reveal(x, y)
    g.print_board()
    if o:
        print("lose")
        break

    if g.win():
        print("win")
        break

