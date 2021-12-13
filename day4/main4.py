from utils import get_lines
from typing import List


NUM_COLS, NUM_ROWS = 5, 5


def day4_part1(filename="input.txt"):
    lines = get_lines(filename)
    # parse input into list of boards
    drawn, boards = parse(lines)
    # print(boards)
    for n in drawn:
        for b in boards:
            r, c = mark(b, n)   # -1, -1 if not found
            if bingo(b, r, c):
                return sum_board(b) * int(n)


def parse(lines: List[str]):
    drawn = lines[0].split(",")
    boards = []
    i = 2
    while i < len(lines):
        curr_board = []
        for j in range(5):
            curr_line = lines[i]
            curr_board.append(curr_line.split())
            i += 1
        boards.append(curr_board)
        i += 1
    return drawn, boards


def mark(board: List[List[str]], n: int) -> (int, int):
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if board[r][c] == n:
                board[r][c] = ""
                return r, c
    return -1, -1


def bingo(board: List[List[str]], r: int, c: int) -> bool:
    # check row
    marked_num = 0
    for i in range(NUM_COLS):
        if not board[r][i]:
            marked_num += 1
    if marked_num == NUM_COLS:
        return True
    # check column
    marked_num = 0
    for j in range(NUM_ROWS):
        if not board[j][c]:
            marked_num += 1
    return marked_num == NUM_ROWS


def sum_board(board: List[List[str]]) -> int:
    total = 0
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            if board[r][c] != "":
                total += int(board[r][c])
    return total


def day4_part2(filename="input.txt"):
    lines = get_lines(filename)
    # parse input into list of boards
    drawn, boards = parse(lines)
    bingod = [False] * len(boards)
    num_bingos = 0
    for n in drawn:
        for i, b in enumerate(boards):
            if not bingod[i]:
                r, c = mark(b, n)   # -1, -1 if not found
                if bingo(b, r, c):
                    bingod[i] = True
                    num_bingos += 1
                    if num_bingos == len(boards):
                        return sum_board(b) * int(n)


if __name__ == "__main__":
    print(day4_part2("input.txt"))

# 18998 is not correct