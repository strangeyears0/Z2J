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

    k = 0
    l = 0
    for j in range(3):
        row_list = []
        for i in range(3):
            row_list.append(board[l][k])
            k = k + 1

            row = ' '.join(row_list)
        print(row)
one_square()
big_board()
print_board()
