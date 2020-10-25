"""
Problem 6:
The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is
    3025 - 385 = 2640

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""

from __future__ import absolute_import, division, print_function


def solution(max_natural_numbers: int = 100) -> int:
    sum_of_squares = 0
    square_of_sums = 0

    for number in range(max_natural_numbers + 1):
        sum_of_squares += number ** 2
        square_of_sums += number

    return square_of_sums ** 2 - sum_of_squares
