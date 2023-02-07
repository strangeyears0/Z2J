import random
import copy

square = []


def square_generator():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for p in range(9):
        copy_numbers = copy.deepcopy(numbers)
        grid = [[0 for x in range(3)] for y in range(3)]
        i = 0
        j = 0


        for o in numbers:
            random_number = random.choice(copy_numbers)
            if random_number in copy_numbers:
                copy_numbers.remove(random_number)
            grid[i][j]=random_number
            i = i +1
            if i == 3:
                j =j +1
                i = 0
        square.append(grid)
    print(square)
def display_board():
    row=[]
    i = 0
    j = 0
    for element in square:
        row.append(element[i][j])
    i = 0
    j= 1
    for element in square:
        row.append(element[i][j])
    i = 0
    j= 2
    for element in square:
        row.append(element[i][j])

    print(row)







square_generator()
display_board()

    # def generate_sudoku():
#
#     grid = [[0 for x in range(3)] for y in range(3)]
#     i = 0
#     j = 0
#
#     for x in numbers:
#
#         random_number = random.choice(copy_numbers)
#
#         grid[i][j]=random_number
#
#         i= i + 1
#         if i == 3:
#             j = j + 1
#             i = 0
#
#
#         if random_number in copy_numbers:
#             copy_numbers.remove(random_number)
#
#
#
#         # big_square.append(grid)
#         # for row in grid:
#         #     print(row)
#         # for square in big_square:
#         #     print(square)
#
#     copy_grid = grid.copy()
#     square.append(copy_grid)
#     copy.deepcopy(numbers)
#
# generate_sudoku()
#
#
# for element in square:
#     print(element)


