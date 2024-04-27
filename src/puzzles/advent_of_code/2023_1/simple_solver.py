"""
This is a solution to https://adventofcode.com/2023/day/1
"""
import re


def answer(data):
    def is_digit(char: str) -> bool:
        return bool(re.match('\d', char))

    def calibration_value(string: str) -> int:
        digits = [char for char in string if is_digit(char)]
        calibration_value = int(digits[0] + digits[-1])
        return calibration_value

    return sum([calibration_value(datum) for datum in data])


with open('test_data.txt') as test_data_file:
    print(answer(test_data_file.readlines()))