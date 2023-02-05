import random
def generate_sudoku():
    grid = [[0 for x in range(9)] for y in range(9)]

    for i in range(9):
        for j in range(9):
            grid[i][j] = random.randint(1,9)
    return grid
sudoku = generate_sudoku()
for element in sudoku:
    print(element)

