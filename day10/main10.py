from utils import get_lines
from typing import List


def dayX_part1(filename="input.txt"):
    lines = get_lines(filename)
    lines = [x.strip() for x in lines]
    values = {")": 3, "]": 57, "}": 1197, ">": 25137}
    match = {")": "(", "]": "[", "}": "{", ">": "<"}
    opening = set(match.values())
    # print(opening)
    total_sum = 0
    for line in lines:
        stack = []
        for c in line:
            if c in opening:
                stack.append(c)
            else:
                # print(c)
                if not stack or match[c] != stack.pop():
                    total_sum += values[c]
                    break
    return total_sum


def dayX_part2(filename="input.txt"):
    lines = get_lines(filename)
    lines = [x.strip() for x in lines]
    values = {"(": 1, "[": 2, "{": 3, "<": 4}
    match = {")": "(", "]": "[", "}": "{", ">": "<"}
    opening = set(match.values())
    # print(opening)
    stack_sums = []
    for line in lines:
        stack = []
        corrupted = False
        for c in line:
            if c in opening:
                stack.append(c)
            else:
                if not stack or match[c] != stack.pop():
                    corrupted = True
                    continue
        # now deal with the stack
        if not corrupted:
            stack_sum = 0
            while stack:
                stack_sum *= 5
                stack_sum += values[stack.pop()]
            stack_sums.append(stack_sum)

    stack_sums.sort()
    print(stack_sums)
    print(len(stack_sums))
    return stack_sums[len(stack_sums)//2]


if __name__ == "__main__":
    # print("DAY 1")
    # print(f"TEST-INPUT: {dayX_part1('test-input.txt')}")
    # print(f"REAL INPUT: {dayX_part1()}")
    print("DAY 2")
    print(f"TEST-INPUT: {dayX_part2('test-input.txt')}")
    print(f"REAL INPUT: {dayX_part2()}")

