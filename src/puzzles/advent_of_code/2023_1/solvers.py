"""
This is a solution to https://adventofcode.com/2023/day/1
"""
import re
from abstract_solver import AbstractSolver


class SolveWithInAndSum(AbstractSolver):
    """
    Make AbstractSolver concrete by writing
    methods for is_digit and solution
    """
    @staticmethod
    def is_digit(char):
        return char in '0123456789'

    def solution(self):
        return sum(self.calibration_value(input_value) for input_value in self.test_data)


class SolveWithIntAndSum(AbstractSolver):
    """
    Make AbstractSolver concrete by writing
    methods for is_digit and solution
    """
    @staticmethod
    def is_digit(char):
        try:
            int(char)
        except ValueError:
            return False
        return True

    def solution(self):
        return sum( (self.calibration_value(input_value)for input_value in self.test_data))


class SolveWithRegexAndSum(AbstractSolver):
    """
    Make AbstractSolver concrete by writing
    methods for is_digit and solution
    """
    @staticmethod
    def is_digit(char):
        # To experiment with regular expressions,
        # this is a great resource: https://regex101.com/
        matches = re.match('\d', char)
        return bool(matches)

    def solution(self):
        return sum(self.calibration_value(input_value) for input_value in self.test_data)


class SolveWithValueAndLoop(AbstractSolver):
    """
    Make AbstractSolver concrete by writing
    methods for is_digit and solution
    """
    @staticmethod
    def is_digit(char):
        # To experiment with regular expressions,
        # this is a great resource: https://regex101.com/
        matches = re.match('\d', char)
        return bool(matches)

    def solution(self):
        running_total = 0  # initialise the answer to 0
        for input_value in self.test_data:  # Loop through the values
            # Add the calibration value to running total
            running_total += self.calibration_value( input_value)

        # The answer to the problem is the running total after we've processed all of the values.
        return running_total



