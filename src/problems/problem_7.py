"""
Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from __future__ import absolute_import, division, print_function


def solution(prime_index: int = 10001) -> int:
    iterator = 3
    valid_primes = [2]

    if prime_index <= 2:
        return prime_index

    while len(valid_primes) < prime_index:
        for valid in valid_primes:
            if iterator % valid == 0:
                break
        else:
            valid_primes.append(iterator)
        iterator += 2

    return valid_primes[-1]
