"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from __future__ import absolute_import, division, print_function

from _core import generate_primes


def solution(limit: int = 2000000):
    primes = generate_primes(limit)
    return sum(primes)
