def get_lines(filename):
    with open(filename) as f:
        input_lines = list(map(lambda x: x.strip(), f.readlines()))
    return input_lines


def get_input_numbers(filename):
    input_numbers = list(map(int, get_lines(filename)))
    return input_numbers


def get_input(filename):
    with open(filename) as f:
        return f.read()
