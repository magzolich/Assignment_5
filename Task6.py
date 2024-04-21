# 6 Eggs hunting II: develop a Guessing Game where players find hidden eggs on a 5x5 board.
import random
row_count = 5
col_count = 5
eggs_count = 10


def create_empty_board():
    board = []
    for row in range(0, row_count):
        board.append([0]*col_count)
    return board


def distribute_eggs(board):
    for i in range(0, eggs_count):
        x = random.randint(0, row_count-1)
        y = random.randint(0, col_count-1)
        while board[x][y] == 1:
            x = random.randint(0, row_count-1)
            y = random.randint(0, col_count-1)
        board[x][y] = 1


def print_board(board):
    for row in range(0, row_count):
        for col in range(0, col_count):
            print(board[row][col], end="")
        print("")


def main():
    board = create_empty_board()
    print_board(board)
    distribute_eggs(board)
    print_board(board)


if __name__ == '__main__':
    main()
