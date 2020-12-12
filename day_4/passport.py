import re
from dataclasses import dataclass


@dataclass(repr=True, eq=True)
class PassportData:
    def __init__(self, string_data):
        fields = re.findall('([a-z]{3}):([a-zA-Z0-9#]*)', string_data)
        for field, value in fields:
            self.__setattr__(field, value)


class Passport:
    def __init__(self, passport_data):
        self.data = passport_data

    def is_valid(self, validate_fields=False):
        return PassportValidator.validate(self, validate_fields=validate_fields)


class PassportValidator:
    __required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    __field_restrictions = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: 150 <= int(
            PassportValidator._remove_unit(x)) <= 193 if 'cm' in x else 59 <= PassportValidator._remove_unit(x) <= 76,
        'hcl': lambda x: re.match(r'#[0-9a-z]{6}', x) is not None,
        'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x: re.match(r'^\d{9}$', x) is not None
    }

    @staticmethod
    def validate(passport, validate_fields=False):
        required_fields_not_empty = all(
            map(lambda x: getattr(passport.data, x, None), PassportValidator.__required_fields))
        if required_fields_not_empty and validate_fields:
            fields_match_requirements = all(
                map(lambda x: PassportValidator.__field_restrictions[x](passport.data.__getattribute__(x)),
                    PassportValidator.__required_fields))
            return fields_match_requirements
        return required_fields_not_empty

    @staticmethod
    def _remove_unit(height):
        return int(height.replace('cm', '').replace('in', ''))
