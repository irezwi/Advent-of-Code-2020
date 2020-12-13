from utils.io import get_lines

ROWS = 128
COLS = 8


def get_part(collection, part):
    border_value = len(collection) // 2
    if part in ['F', 'L']:
        return collection[:border_value]
    elif part in ['B', 'R']:
        return collection[border_value:]
    else:
        raise Exception('Not supported part given')


def execute_instructions(collection, instructions):
    for instruction in instructions:
        collection = get_part(collection, instruction)
    return collection[0]


def get_seat_id(instructions):
    row_instructions, col_instructions = instructions
    row = execute_instructions(list(range(ROWS)), row_instructions)
    col = execute_instructions(list(range(COLS)), col_instructions)
    return row * 8 + col


lines = get_lines("input.txt")
instructions_list = list(map(lambda x: (x[:7], x[7:]), lines))
print(f'Part 1 solution: {max(map(get_seat_id, instructions_list))}')

occupied = set(map(get_seat_id, instructions_list))
my_spot = next(filter(
    lambda x: x not in occupied and x - 1 in occupied and x + 1 in occupied, range(min(occupied), max(occupied))))
print(f'Part 2 solution: {my_spot}')
