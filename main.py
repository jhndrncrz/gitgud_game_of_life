import random
import os
import time

## TODO
# (done) branch: fix bug
# (done) merge fix bug branch
#
# commit: allow user input for board size
# commit: add validation for inputs
#
# branch: implement colors feature
#       commit: add ansi colors dictionary
#       commit: add one color to all cells
#       commit: add random color to every cell
#
# branch: implement iteration counter
#       (done) commit: add iteration counter
#       (done) commit: center iteration counter
# 
# commit: remove file.txt
# commit: retrieve file.txt from previous commit
#
# merge iteration counter branch
# rebase colors branch

def create_grid(rows: int, columns: int) -> list[list[int]]:
    return [[random.choice([0, 1]) for _ in range(columns)] for _ in range(rows)]

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
    counter: int = 0
    padding: int = ((columns * 2) - 2 - len(f"ITERATION {counter}")) // 2
    while True:
        print_grid(grid)
        print(f"{" " * padding}ITERATION {counter}{" " * padding}")
        grid = update_grid(grid)
        time.sleep(0.25)
        counter += 1

def main():
    rows: int = int(input("Enter rows: "))
    columns: int = int(input("Enter columns: "))
    game_of_life(rows, columns)

if __name__ == '__main__':
    main()
