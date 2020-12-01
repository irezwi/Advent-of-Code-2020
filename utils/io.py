def get_input_numbers():
    with open('input.txt') as f:
        input_numbers = list(map(int, map(lambda x: x.strip(), f.readlines())))
    return input_numbers
