import re
from functools import reduce

from utils.io import get_lines


def is_password_valid_part_1(input_line):
    count_min, count_max, letter, password = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', input_line).groups()
    return int(count_min) <= password.count(letter) <= int(count_max)


def is_password_valid_part_2(input_line):
    position_a, position_b, letter, password = re.search(r'(\d+)-(\d+) ([a-z]): ([a-z]+)', input_line).groups()
    return (password[int(position_a) - 1] == letter) ^ (password[int(position_b) - 1] == letter)


print(reduce(lambda x, y: x + y, map(is_password_valid_part_1, get_lines("input.txt"))))
print(reduce(lambda x, y: x + y, map(is_password_valid_part_2, get_lines("input.txt"))))
