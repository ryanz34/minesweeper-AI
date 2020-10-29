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
    if hidden_board[y][x]:
        hidden_board[y][x] = False

    if game_board[y][x] == 9:
        return True
    else:
        return False


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


