from utils.io import get_input_numbers


def find_product_of_2_that_sum_up_to_2020(numbers):
    for first in numbers:
        for second in numbers:
            if second + first == 2020:
                return second * first


def find_product_of_3_that_sum_up_to_2020(numbers):
    for first in numbers:
        for second in numbers:
            for third in numbers:
                if third + second + first == 2020:
                    return third * second * first


print(f'Part 1 solution: {find_product_of_2_that_sum_up_to_2020(get_input_numbers())}')
print(f'Part 2 solution: {find_product_of_3_that_sum_up_to_2020(get_input_numbers())}')
