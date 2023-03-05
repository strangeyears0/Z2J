import random


def create_board():
    # Creates board 9x9 and fill with 0.
    board = [[0 for x in range(9)] for y in range(9)]
    fill_board(board)


def fill_board(board):
    # Fill 3x3 squares with numbers 1-9.
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(numbers)
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    board[x][y] = numbers.pop()
    print_board(board)
    menu(board)


def print_board(board):
    # Prints board and adds marks to separate 3x3 squares.
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j, value in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(value, end=" ")
        print()


def menu(board):
    # Prints menu and options.
    print("- " * 11)
    check = input('\nMENU:\n1. Check rows\n2. Check columns\n3. Generate again\n4. Quit\n\n\tYour choice: ')
    if check == '1':
        check_rows(board)
    elif check == '2':
        check_cols(board)
    elif check == '3':
        create_board()
    elif check == '4':
        quit()
    else:
        print('Choose correct option number.')
        menu(board)


def check_rows(board):
    # Checks the rows if follows the rules of Sudoku.
    row_num = 0
    for row in board:
        row_num += 1
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(f'Row {row_num} does not follow the rules of Sudoku.')
        else:
            print(f'Row {row_num} follows the rules of Sudoku.')
    menu(board)


def check_cols(board):
    # Checks the columns if follows the rules of Sudoku.
    col_num = 0
    for col_idx in range(9):
        col = [board[row_idx][col_idx] for row_idx in range(9)]
        if sorted(col) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            col_num += 1
            print(f'Column {col_num} does not follow the rules of Sudoku.')
        else:
            print(f'Column {col_num} follows the rules of Sudoku.')
    menu(board)


create_board()
