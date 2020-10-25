"""
Problem 5:
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""

from __future__ import absolute_import, division, print_function

import math

from _core import generate_primes


def solution(divisor_max=20) -> int:
    result = 1
    prime_numbers = generate_primes(limit=divisor_max)

    for index in range(len(prime_numbers)):
        a = int(math.floor(math.log(divisor_max) / math.log(prime_numbers[index])))
        result = result * int(math.pow(prime_numbers[index], a))

    return result
