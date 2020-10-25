"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

from __future__ import absolute_import, print_function, division

import math


def solution(input_number: int = 600851475143) -> int:
    result = 0
    for factor in range(3, int(math.sqrt(input_number)) + 1, 2):
        while input_number % factor == 0:
            result = factor
            input_number = input_number / factor

    if input_number > 2:
        return input_number

    return result
