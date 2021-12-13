from utils import get_lines
from typing import List, Tuple


# non-optimal solution
# we're just brute-forcing our way across, marking every single cell


def day5_part1(filename="input.txt"):
    if filename == "input.txt":
        num_cols, num_rows = 1000, 1000
    else:
        num_cols, num_rows = 10, 10
    lines = get_lines(filename)
    segments = parse(lines)
    matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    results = 0

    for segment in segments:
        results += mark(matrix, segment)

    return results


def day5_part2(filename="input.txt"):
    if filename == "input.txt":
        num_cols, num_rows = 1000, 1000
    else:
        num_cols, num_rows = 10, 10
    lines = get_lines(filename)
    segments = parse(lines)
    matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    results = 0

    for segment in segments:
        results += mark_part2(matrix, segment)

    return results


def parse(lines: List[str]) -> List[List[int]]:
    result = []
    for line in lines:
        source, dest = line.split("->")
        x1, y1 = source.split(",")
        x2, y2 = dest.split(",")
        result.append([int(x1), int(y1), int(x2), int(y2)])
    return result


def mark(matrix: List[List[int]], segment: List[int]) -> int:
    x1, y1, x2, y2 = segment
    overlap_count = 0
    if x1 == x2:
        # make y1 smaller
        y1, y2 = (y1, y2) if y1 < y2 else (y2, y1)
        for i in range(y1, y2 + 1):
            matrix[i][x1] += 1
            if matrix[i][x1] == 2:
                overlap_count += 1
    elif y1 == y2:
        x1, x2 = (x1, x2) if x1 < x2 else (x2, x1)
        for j in range(x1, x2 + 1):
            matrix[y1][j] += 1
            if matrix[y1][j] == 2:
                overlap_count += 1
    return overlap_count


def mark_part2(matrix: List[List[int]], segment: List[int]) -> int:
    x1, y1, x2, y2 = segment
    overlap_count = 0
    if x1 == x2:
        # make y1 smaller
        y1, y2 = (y1, y2) if y1 < y2 else (y2, y1)
        for i in range(y1, y2 + 1):
            matrix[i][x1] += 1
            if matrix[i][x1] == 2:
                overlap_count += 1
    elif y1 == y2:
        x1, x2 = (x1, x2) if x1 < x2 else (x2, x1)
        for j in range(x1, x2 + 1):
            matrix[y1][j] += 1
            if matrix[y1][j] == 2:
                overlap_count += 1
    else:
        # swap so always pointing NE or SE
        x1, y1, x2, y2 = (x1, y1, x2, y2) if x1 < x2 else (x2, y2, x1, y1)
        if y2 > y1:
            inc = 1
        else:
            inc = -1
        while x1 <= x2:  # we don't check y, we just trust the input that both will be equal at same time
            matrix[y1][x1] += 1
            if matrix[y1][x1] == 2:
                overlap_count += 1
            x1 += 1
            y1 += inc
    return overlap_count


# 19635 incorrect


if __name__ == "__main__":
    # print(day5_part2("test-input.txt"))
    print(day5_part2("input.txt"))
