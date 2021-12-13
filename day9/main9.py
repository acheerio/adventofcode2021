from utils import get_lines
import heapq
from collections import deque


def day9_part1(filename="input.txt"):
    lines = get_lines(filename)
    heightmap = []
    for line in lines:
        heightmap.append([int(x) for x in line.strip()])
    num_rows, num_cols = len(heightmap), len(heightmap[0])
    # print(heightmap)
    # print(num_rows)
    # print(num_cols)

    total_sum = 0
    for r in range(num_rows):
        for c in range(num_cols):
            is_low_point = True
            for next_r, next_c in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                if 0 <= next_r < num_rows and 0 <= next_c < num_cols:
                    # print(f"next_r: {next_r}, next_c: {next_c}")
                    if heightmap[r][c] >= heightmap[next_r][next_c]:
                        is_low_point = False
                        break
            if is_low_point:
                total_sum += (heightmap[r][c] + 1)
    return total_sum


def day9_part2(filename="input.txt"):
    lines = get_lines(filename)
    heightmap = []
    for line in lines:
        heightmap.append([int(x) for x in line.strip()])
    num_rows, num_cols = len(heightmap), len(heightmap[0])
    heap = []

    for r in range(num_rows):
        for c in range(num_cols):
            is_low_point = True
            for next_r, next_c in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
                if 0 <= next_r < num_rows and 0 <= next_c < num_cols:
                    # print(f"next_r: {next_r}, next_c: {next_c}")
                    if heightmap[r][c] >= heightmap[next_r][next_c]:
                        is_low_point = False
                        break
            if is_low_point:
                basin_size = get_basin_size(heightmap, r, c)
                heapq.heappush(heap, basin_size)
                if len(heap) > 3:
                    heapq.heappop(heap)
    return heap[0] * heap[1] * heap[2]


def get_basin_size(heightmap, start_r, start_c):
    q = deque()
    q.append((start_r, start_c))
    heightmap[start_r][start_c] = -1
    num_rows, num_cols = len(heightmap), len(heightmap[0])
    curr_size = 0

    while q:
        r, c = q.popleft()
        curr_size += 1
        for next_r, next_c in ((r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)):
            if 0 <= next_r < num_rows and 0 <= next_c < num_cols:
                if heightmap[next_r][next_c] != 9 and heightmap[next_r][next_c] != -1:
                    heightmap[next_r][next_c] = -1  # visited
                    q.append((next_r, next_c))
    return curr_size


if __name__ == "__main__":
    print("PART 1")
    print(f"TEST-INPUT: {day9_part1('test-input.txt')}")
    print(f"REAL INPUT: {day9_part1()}")
    print("PART 2")
    print(f"TEST-INPUT: {day9_part2('test-input.txt')}")
    print(f"REAL INPUT: {day9_part2()}")

