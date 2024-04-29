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


def print_board(board, guesses):
    for row in range(0, row_count):
        for col in range(0, col_count):
            if {'x': row, 'y': col} in guesses:
                if (board[row][col] == 1):
                    print('0', end="")
                else:
                    print('X', end="")
            else:
                print('.', end="")
        print("")


def user_input(guesses):
    x = int(input("x"))
    y = int(input("y"))
    point = {'x': x, 'y': y}
    if point in guesses:
        print("You've already tried this field, select another field")
    else:
        guesses.append(point)


def main():
    board = create_empty_board()
    distribute_eggs(board)
    guesses = []
    all_eggs_found = False
    while not all_eggs_found:
        print_board(board, guesses)
        user_input(guesses)
        print_board(board, guesses)
        all_eggs_found = len(list(filter(
            lambda point: board[point['x']][point['y']] == 1, guesses))) == eggs_count


if __name__ == '__main__':
    main()
