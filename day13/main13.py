from utils import get_lines
from typing import List, Tuple


def day13_part1(filename="input.txt"):
    lines = get_lines(filename)
    dots, instructions = parse(lines)
    grid = make_grid(dots)
    axis, coord = instructions[0]
    grid = execute_fold(grid, axis, coord)
    return count_dots(grid)


def parse(lines: List[str]) -> (List[List[int]], List[Tuple[str, int]]):
    dots = []
    instructions = []
    is_instruction = False
    for line in lines:
        if line == "\n":
            is_instruction = True
            continue
        if is_instruction:
            _, _, equation = line.strip().split()
            axis, coord = equation.split("=")
            instructions.append((axis, int(coord)))
        else:
            x, y = line.strip().split(",")
            dots.append([int(x), int(y)])
    return dots, instructions


def make_grid(coordinates: List[List[int]]) -> List[List[str]]:
    num_rows, num_cols = 0, 0
    for x, y in coordinates:
        num_rows = max(num_rows, y)
        num_cols = max(num_cols, x)
    num_rows += 1
    num_cols += 1
    matrix = [["." for _ in range(num_cols)] for _ in range(num_rows)]
    for x, y in coordinates:
        matrix[y][x] = "#"
    return matrix


def execute_fold(grid, axis, coord):
    if axis == "x":
        return execute_x_fold(grid, coord)
    elif axis == "y":
        return execute_y_fold(grid, coord)


def execute_x_fold(grid, fold_coord):
    num_rows, num_cols = len(grid), len(grid[0])
    new_num_cols = fold_coord
    new_grid = [["." for _ in range(new_num_cols)] for _ in range(num_rows)]
    for r in range(0, num_rows):
        for c in range(fold_coord + 1, num_cols):
            if grid[r][c] == "#":
                new_c = fold_coord - (c - fold_coord)
                if new_c >= 0:
                    new_grid[r][new_c] = "#"
    for r in range(0, num_rows):
        for c in range(0, new_num_cols):
            if grid[r][c] == "#":
                new_grid[r][c] = "#"
    return new_grid


def execute_y_fold(grid, fold_coord):
    num_rows, num_cols = len(grid), len(grid[0])
    new_num_rows = fold_coord
    new_grid = [["." for _ in range(num_cols)] for _ in range(new_num_rows)]
    for r in range(fold_coord, num_rows):
        for c in range(num_cols):
            if grid[r][c] == "#":
                new_r = fold_coord - (r - fold_coord)
                if new_r >= 0:
                    new_grid[new_r][c] = "#"
    for r in range(0, new_num_rows):
        for c in range(0, num_cols):
            if grid[r][c] == "#":
                new_grid[r][c] = "#"
    return new_grid


def count_dots(grid):
    num_rows, num_cols = len(grid), len(grid[0])
    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if grid[r][c] == "#":
                count += 1
    return count


def print_grid(grid: List[List[str]]):
    for row in grid:
        print("".join(row))


def day13_part2(filename="input.txt"):
    lines = get_lines(filename)
    dots, instructions = parse(lines)
    grid = make_grid(dots)
    for axis, coord in instructions:
        grid = execute_fold(grid, axis, coord)
    print_grid(grid)


if __name__ == "__main__":
    print("PART 1")
    print(f"TEST-INPUT: {day13_part1('test-input.txt')}")
    print(f"REAL INPUT: {day13_part1()}")
    print("PART 2")
    day13_part2('test-input.txt')
    day13_part2()


