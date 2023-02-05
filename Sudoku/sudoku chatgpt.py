import random

def generate_sudoku():
    grid = [[0 for x in range(9)] for y in range(9)]
    fill_sudoku(grid, 0, 0)
    return grid

def fill_sudoku(grid, i, j):
    if i == 9:
        return True
    if j == 9:
        return fill_sudoku(grid, i + 1, 0)
    if grid[i][j] != 0:
        return fill_sudoku(grid, i, j + 1)
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(nums)
    for num in nums:
        if is_valid(grid, i, j, num):
            grid[i][j] = num
            if fill_sudoku(grid, i, j + 1):
                return True
            grid[i][j] = 0
    return False

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num:
            return False
    for i in range(9):
        if grid[i][col] == num:
            return False
    square_x = (row // 3) * 3
    square_y = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[square_x + i][square_y + j] == num:
                return False
    return True

grid = generate_sudoku()
for row in grid:
    print(row)