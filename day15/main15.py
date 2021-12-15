from utils import get_lines
import math
import heapq


def parse_input(filename):
    lines = get_lines(filename)
    matrix = []
    for line in lines:
        matrix.append([int(c) for c in line.strip()])
    return matrix


def get_min_risk(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])
    heap = [(0, 0, 0)]  # risk, row, col
    risk = dict()
    risk[(0, 0)] = 0
    visited = set()
    while heap:
        curr_risk, row, col = heapq.heappop(heap)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for next_row, next_col in [(row, col + 1), (row, col - 1), (row - 1, col), (row + 1, col)]:
            if 0 <= next_row < num_rows and 0 <= next_col < num_cols and (next_row, next_col) not in visited:
                next_risk = math.inf if (next_row, next_col) not in risk else risk[(next_row, next_col)]
                next_risk = min(curr_risk + matrix[next_row][next_col], next_risk)
                risk[(next_row, next_col)] = next_risk
                heapq.heappush(heap, (next_risk, next_row, next_col))
    return risk[(len(matrix) - 1, len(matrix[0]) - 1)]


def day15_part1_try3(filename="input.txt"):
    matrix = parse_input(filename)
    return get_min_risk(matrix)


def day15_part1_try2(filename="input.txt"):
    matrix = parse_input(filename)
    num_rows, num_cols = len(matrix), len(matrix[0])
    dp = [[math.inf for _ in range(num_cols + 1)] for _ in range(num_rows + 1)]
    dp[1][1] = 0
    for r in range(1, num_rows + 1):
        for c in range(1, num_cols + 1):
            if r == 1 and c == 1:
                continue
            dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + matrix[r - 1][c - 1]
    return dp[-1][-1]


def backtrack(grid, curr_row, curr_col, curr_sum, min_sum):
    num_rows, num_cols = len(grid), len(grid[0])
    if curr_row == num_rows - 1 and curr_col == num_cols - 1:
        min_sum[0] = min(min_sum[0], curr_sum)
        print(f"Got to end, sum was {curr_sum}")
        return

    for next_row, next_col in [(curr_row + 1, curr_col), (curr_row, curr_col + 1)]:
        if 0 <= next_row < num_rows and 0 <= next_col < num_cols:
            backtrack(grid, next_row, next_col, curr_sum + grid[next_row][next_col], min_sum)


def day15_part1_try1(filename="input.txt"):
    matrix = parse_input(filename)
    min_sum = [math.inf]
    backtrack(matrix, 0, 0, 0, min_sum)
    return min_sum[0]


def day15_part2(filename="input.txt"):
    matrix = parse_input(filename)
    matrix = expand(matrix)
    return get_min_risk(matrix)


def expand(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])
    new_matrix = [[0 for _ in range(num_cols * 5)] for _ in range(num_rows * 5)]
    for r in range(num_rows):
        for c in range(num_cols):
            for i in range(5):
                for j in range(5):
                    if i == 0:
                        new_value = matrix[r][c] + j
                    elif j == 0:
                        new_value = matrix[r][c] + i
                    else:
                        new_value = new_matrix[r + (i - 1) * num_cols][c + j * num_rows] + 1
                    if new_value > 9:
                        new_value -= 9
                    new_matrix[r + i * num_cols][c + j * num_rows] = new_value
    return new_matrix


if __name__ == "__main__":
    print("PART 1")
    print(f"TEST-INPUT: {day15_part1_try3('test-input.txt')}")
    print(f"REAL INPUT: {day15_part1_try3()}")
    print("PART 2")
    print(f"TEST-INPUT: {day15_part2('test-input.txt')}")
    print(f"REAL INPUT: {day15_part2()}")

