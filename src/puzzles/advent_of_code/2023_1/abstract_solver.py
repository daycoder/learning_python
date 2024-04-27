"""
This is a solution to https://adventofcode.com/2023/day/1
"""
import re
from abc import ABC, abstractmethod


class AbstractSolver(ABC):
    """
    This class gets us the following:
        * reads the test data
        * teh calibration_value method process
          one lie of the test data
        * placeholders (abstract methods) that
          we can fill in later (make concrete) for
            * is_digit
            * solution
    """
    def __init__(self):
        with open('test_data.txt') as test_data_file:
            self.test_data = test_data_file.readlines()

    @staticmethod  # <- if static and abstract, static must come first!
    @abstractmethod
    def is_digit(char: str) -> bool:
        pass

    @abstractmethod
    def solution(self) -> int:
        pass

    @classmethod
    def calibration_value(cls, string: str) -> int:
        digits = [char for char in string if cls.is_digit(char)]
        calibration_value = int(digits[0]+digits[-1])
        return calibration_value
