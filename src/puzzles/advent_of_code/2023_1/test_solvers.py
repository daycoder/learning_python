"""
This is a solution to https://adventofcode.com/2023/day/1
"""
from solvers import (
    SolveWithInAndSum,
    SolveWithIntAndSum,
    SolveWithRegexAndSum,
    SolveWithValueAndLoop
)


def verify_calibration_value(solver):
    # test calibration_value with known test data
    TEST_DATA = [('1abc2', 12),
                 ('pqr3stu8vwx', 38),
                 ('a1b2c3d4e5f', 15),
                 ('treb7uchet', 77)]

    for input_value, expected in TEST_DATA:
        assert solver.calibration_value(input_value) == expected


def verify_solvers(*solvers):
    for solver in solvers:
        verify_calibration_value(solver)

    results = {solver: solver().solution() for solver in solvers}
    assert len(set(results.values())) == 1, f'All results should match. Got {results}'
    print(f'Result:{list(results.values())[0]}')


verify_solvers(
    SolveWithInAndSum,
    SolveWithIntAndSum,
    SolveWithRegexAndSum,
    SolveWithValueAndLoop,
)




