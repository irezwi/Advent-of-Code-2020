from utils.io import get_input
from day_4.passport import Passport, PassportData, PassportValidator

passports_lines = map(lambda x: " ".join(x), map(lambda x: x.split('\n'), get_input('input.txt').split('\n\n')))

passports = [Passport(PassportData(line)) for line in passports_lines]
print(f'Part 1 solution: {len(list(filter(lambda x: x.is_valid(), passports)))}')
print(f'Part 2 solution: {len(list(filter(lambda x: x.is_valid(validate_fields=True), passports)))}')

a = 0
