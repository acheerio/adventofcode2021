import math
from collections import deque


def day1_part1(input="input.txt"):
    increase_count = 0
    with open(input) as f:
        lines = f.readlines()
    prev_depth = math.inf

    print(lines)
    for line in lines:
        curr_depth = int(line)
        if curr_depth > prev_depth:
            increase_count += 1
        prev_depth = curr_depth
    return increase_count


def day1_part2(input="input.txt"):
    increase_count = 0
    with open(input) as f:
        lines = f.readlines()
    prev_depths = deque()
    prev_depths.extend([int(x) for x in lines[:3]])
    for i in range(3, len(lines)):
        curr_depth = int(lines[i])
        curr_sum = prev_depths[1] + prev_depths[2] + curr_depth
        if curr_sum > sum(prev_depths):
            increase_count += 1
        prev_depths.append(curr_depth)
        prev_depths.popleft()
    return increase_count


print(day1_part2("input.txt"))