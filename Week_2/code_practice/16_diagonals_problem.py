# grid_generator function is using list comprehension syntax to generate matrix.
# [[0 for x in range(cols_count)] for x in range(rows_count)]
def grid_generator(grid_len):
    grid = [[-1 for x in range(grid_len)] for x in range(grid_len)]
    return grid

def display_grid(grid):
    for row in range(len(grid)):
        print(grid[row])

def diagonals_problem(grid_len, diagonals_num):
    grid = grid_generator(grid_len)
    valid_diagonals = 0
    sol_num = 0

    if valid_diagonals == diagonals_num:
        sol_num += 1
        display_grid(grid)
        return
    
    
# matrix = grid_generator(5)

# for row in range(len(matrix)):
#     print(matrix[row])

