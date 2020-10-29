from random import choice


def print_board(game_board, marked_board, hidden_board):
    for y in range(len(game_board)):
        for x in range(len(game_board[0])):
            if marked_board[y][x]:
                print("M", end="")
            elif hidden_board[y][x]:
                print("*", end="")
            else:
                print(game_board[y][x], end="")
        print()


def compute_neighbours(game_board):
    for y in range(len(game_board)):
        for x in range(len(game_board[0])):

            if game_board[y][x] != 9:
                bomb_num = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x+i < len(game_board[0]) and 0 <= y+j < len(game_board):
                            if game_board[y+j][x+i] == 9:
                                bomb_num += 1

                game_board[y][x] = bomb_num


def reveal(game_board, masked_board, hidden_board, x, y):
    visit = {(x, y)}
    to_visit = [(x, y)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while len(to_visit) != 0:
        position = to_visit.pop(0)

        hidden_board[position[1]][position[0]] = False

        if game_board[position[1]][position[0]] == 0:
            for d in direction:
                if 0 <= position[0]+d[0] < len(game_board[0]) and 0 <= position[1]+d[1] < len(game_board):
                    p = (position[0]+d[0], position[1]+d[1])

                    if p not in visit:
                        to_visit.append(p)
                        visit.add(p)

    if game_board[y][x] == 9:
        return True


def win(game_board, hidden_board):
    for y in range(len(game_board)):
        for x in range(len(game_board[0])):
            if game_board[y][x] != 9 and hidden_board[y][x]:
                return False
    return True


xdim = int(input("X-dimension: "))
ydim = int(input("Y-dimension: "))
bomb = int(input("Number of bombs: "))

chosenSpots = []
boardSpots = [i for i in range(xdim*ydim)]


for k in range(bomb):
    pos = choice(boardSpots)

    chosenSpots.append(pos)
    boardSpots.remove(pos)

board = [[0]*xdim for _ in range(ydim)]
hboard = [[True]*xdim for _ in range(ydim)]
mboard = [[False]*xdim for _ in range(ydim)]

for i in chosenSpots:
    board[i // xdim][i % xdim] = 9

compute_neighbours(board)
print_board(board, mboard, hboard)

while True:
    x = int(input())
    y = int(input())

    f = reveal(board, mboard, hboard, x, y)
    print_board(board, mboard, hboard)

    if f:
        print("lose")
        break

    if win(board, hboard):
        print("win")
