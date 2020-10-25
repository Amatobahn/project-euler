"""
Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2
For example, 3**2 + 4**2 == 9 + 16 = 25 == 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from __future__ import absolute_import, division, print_function

import math


def solution(target_value=1000) -> int:
    for a in range(1, (target_value // 3) - 1):
        for b in range (a + 1, int(math.ceil((1000 - a) / 2.-1))):
            c = target_value - a - b
            if (a ** 2 + b ** 2) == c ** 2:
                return a * b * c

    return 0
