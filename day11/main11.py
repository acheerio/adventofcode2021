from utils import get_lines
from typing import List
from collections import deque

FLASHING_NUM = 10


def day11_part1(filename="input.txt"):
    unparsed_lines = get_lines(filename)
    grid = [[int(n) for n in s.strip()] for s in unparsed_lines]
    num_flashes = 0

    for i in range(100):
        num_flashes += step(grid)
    return num_flashes


def step(grid: List[List[int]]) -> int:
    num_rows, num_cols = len(grid), len(grid[0])
    flashed = set()
    for curr_r in range(num_rows):
        for curr_c in range(num_cols):
            if (curr_r, curr_c) not in flashed:
                grid[curr_r][curr_c] += 1
                if grid[curr_r][curr_c] == FLASHING_NUM:
                    q = deque()
                    q.append((curr_r, curr_c))
                    flashed.add((curr_r, curr_c))
                    while q:
                        r, c = q.pop()
                        for adj_r, adj_c in [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c), (r - 1, c - 1), (r + 1, c + 1), (r - 1, c + 1), (r + 1, c - 1)]:
                            if 0 <= adj_r < num_rows and 0 <= adj_c < num_cols and (adj_r, adj_c) not in flashed:
                                grid[adj_r][adj_c] += 1
                                if grid[adj_r][adj_c] == FLASHING_NUM:
                                    flashed.add((adj_r, adj_c))
                                    q.append((adj_r, adj_c))
    for r, c in flashed:
        grid[r][c] = 0
    return len(flashed)


def day11_part2(filename="input.txt"):
    unparsed_lines = get_lines(filename)
    grid = [[int(n) for n in s.strip()] for s in unparsed_lines]
    grid_size = len(grid) * len(grid[0])

    for i in range(500):
        num_flashes = step(grid)
        if num_flashes == grid_size:
            return i
    return -1


if __name__ == "__main__":
    # print("DAY 1")
    # print(f"TEST-INPUT: {day11_part1('test-input.txt')}")
    # print(f"REAL INPUT: {day11_part1()}")
    print("DAY 2")
    print(f"TEST-INPUT: {day11_part2('test-input.txt')}")
    print(f"REAL INPUT: {day11_part2()}")

