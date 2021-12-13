from utils import get_lines


def day3part1(filename="input.txt"):
    lines = get_lines(filename)
    input_len = len(lines[0]) - 1 # remove newline
    count_ones, count_zeros = [0] * input_len, [0] * input_len

    # count
    for line in lines:
        for i, c in enumerate(line):
            if c == "0":
                count_zeros[i] += 1
            elif c == "1":
                count_ones[i] += 1


    # get the maxes and mins
    gamma_list, epsilon_list = [], []
    for one_count, zero_count in zip(count_ones, count_zeros):
        if one_count >= zero_count:
            gamma_list.append("1")
            epsilon_list.append("0")
        else:
            gamma_list.append("0")
            epsilon_list.append("1")
    gamma_val = int("".join(gamma_list), 2)
    epsilon_val = int("".join(epsilon_list), 2)
    return gamma_val * epsilon_val


def day3part2(filename="input.txt"):
    lines = get_lines(filename)
    oxygen_rating = get_oxygen_rating(lines[:])
    co2_rating = get_co2_rating(lines[:])
    return oxygen_rating * co2_rating


def get_oxygen_rating(lines):
    curr_index = 0
    rating = []
    while len(lines) > 1:  # seg fault if there are duplicates
        count_zeros, count_ones = get_counts(lines, curr_index)
        value = "0"
        if count_ones >= count_zeros:
            value = "1"
        lines = filter_lines(lines, curr_index, value)
        curr_index += 1
    return int(lines[0], 2)


def get_co2_rating(lines):
    curr_index = 0
    rating = []
    while len(lines) > 1:  # seg fault if there are duplicates
        count_zeros, count_ones = get_counts(lines, curr_index)
        value = "0"
        if count_zeros > count_ones:
            value = "1"
        lines = filter_lines(lines, curr_index, value)
        curr_index += 1
    return int(lines[0], 2)


def get_counts(lines, index):
    count_zeros, count_ones = 0, 0
    for line in lines:
        if line[index] == "0":
            count_zeros += 1
        elif line[index] == "1":
            count_ones += 1
    return count_zeros, count_ones


def filter_lines(lines, curr_index, value):
    result = []
    for line in lines:
        if line[curr_index] == value:
            result.append(line)
    return result


if __name__ == "__main__":
    print(day3part2("input.txt"))