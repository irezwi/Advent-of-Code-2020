from functools import reduce
from collections import Counter

from utils.io import get_input

groups = get_input("input.txt").split("\n\n")

groups_sets = map(lambda x: set(x), map(lambda x: x.replace('\n', ''), groups))
sum_of_answers = reduce(lambda x, y: x + y, map(len, groups_sets))
print(f'Part 1 solution {sum_of_answers}')

people_in_groups = map(lambda x: len(x.split('\n')), groups)
groups_answers = map(lambda x: x.replace('\n', ''), groups)
common_answers = []

for group_answer, people_count in zip(groups_answers, people_in_groups):
    counter = 0
    letter_counter = Counter(group_answer)
    for letter in set(group_answer):
        if letter_counter[letter] == people_count:
            counter += 1
    common_answers.append(counter)

print(f'Part 2 solution: {sum(common_answers)}')
