import random
import os
import time

# 1. branch: fix bug
#
# 2. branch: implement colors feature
#       commit: add ansi colors dictionary
#       commit: add one color to all cells
#       commit: add random color to every cell
#
# 3. branch: implement iteration counter
#       commit: add iteration counter
#       commit: center iteration counter
#
# 4. merge fix bug branch
# 5. rebase colors branch
# 6. merge interation counter branch
#
# 7. commit: allow user input for board size
# 8. commit: add validation for inputs

def create_grid(rows: int, columns: int) -> list[list[int]]:
    return [[random.choice([0, 2]) for _ in range(columns)] for _ in range(rows)]

def print_grid(grid: list[list[int]]) -> None:
    os.system('clear' if os.name == 'posix' else 'cls')
    for row in grid:
        print(' '.join(['*' if cell else ' ' for cell in row]))
    print('\n')

def get_neighbors(grid: list[list[int]], row: int, column: int):
    neighbors: list[int] = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbors.append(grid[(row + i) % len(grid)][(column + j) % len(grid[0])])
    return neighbors

def update_grid(grid):
    new_grid: list[list[int]] = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            alive_neighbors: int = sum(get_neighbors(grid, i, j))
            if grid[i][j]:
                new_grid[i][j] = 1 if 2 <= alive_neighbors <= 3 else 0
            else:
                new_grid[i][j] = 1 if alive_neighbors == 3 else 0
    return new_grid

def game_of_life(rows: int, columns: int):
    grid: list[list[int]] = create_grid(rows, columns)

    while True:
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.25)

def main():
    game_of_life(20, 40)

if __name__ == '__main__':
    main()
