import random

board = []

def one_square():
    numbers = ['1','2','3','4','5','6','7','8','9']
    square = []
    for i in range(9):
        number = random.choice(numbers)
        square.append(number)
        if number in numbers:
            numbers.remove(number)
    return square

def big_board():
    for j in range(9):
        one_square()
        board.append(one_square())
    return board


def print_board():
    i = 0
    j = 0
    for w in range(3):
        for x in  range(3):
            row_list = []
            for y in range(3):
                if y == 0:
                    i = 3 * w
                    j = x * 3
                for z in range(3):
                    row_list.append(board[i][j])
                    j = j + 1
                i = i + 1
                j = j - 3
            row = ' | '.join(row_list)
            print( row )

def verification_row():
    i = 0
    j = 0
    for w in range(3):
        for x in  range(3):
            row_list = []
            for y in range(3):
                if y == 0:
                    i = 3 * w
                    j = x * 3
                for z in range(3):
                    row_list.append(board[i][j])
                    j = j + 1
                i = i + 1
                j = j - 3
            for elem in row_list:
                if row_list.count(elem) > 1:
                    print("The row does not meet the assumptions of the sudoku game:")
                    print(row_list)
                    menu()

def verification_column():
    i = 0
    j = 0
    for w in range(3):
        for x in  range(3):
            column_list = []
            for y in range(3):
                if y == 0:
                    i = w
                    j = x
                for z in range(3):
                    column_list.append(board[i][j])
                    j = j + 3
                i = i + 3
                j = j - 9
            for elem in column_list:
                if column_list.count(elem) > 1:
                    print("The column does not meet the assumptions of the sudoku game:")
                    print(column_list)
                    menu()

def menu():
    print("""
        1 - Generate Sudoku Board
        2 - Check the correctness of the columns
        3 - Check the correctness of the rows
        4 - Quit""")
    x = input("\t\tChoose Action (1-4)")

    if x == '1':
        return one_square(), big_board(), print_board(), menu()
    elif x == '2':
        try:
            return verification_column()
        except:
            print("Sudoku board is not generated! ")
    elif x == '3':
        try:
            return verification_row()
        except:
            print("Sudoku board is not generated!")
    elif x == '4':
        return quit()

    else:
        print("Bad Action")
        return menu()

menu()