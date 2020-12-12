from utils.io import get_input_numbers
from itertools import permutations
from functools import reduce
from typing import List, Optional


def find_product_of_n_nums_that_sum_up_to_2020(numbers: List[int], n: int) -> Optional[int]:
    for permutation in permutations(numbers, n):
        if sum(permutation) == 2020:
            return reduce(lambda x, y: x * y, permutation)
    return None


print(f'Part 1 solution: {find_product_of_n_nums_that_sum_up_to_2020(get_input_numbers("input.txt"), 2)}')
print(f'Part 2 solution: {find_product_of_n_nums_that_sum_up_to_2020(get_input_numbers("input.txt"), 3)}')
