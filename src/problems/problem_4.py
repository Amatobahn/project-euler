"""
Problem 4:
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from __future__ import absolute_import, print_function, division


def solution() -> int:
    def _is_palindrome(value: int) -> bool:
        return True if str(value) == str(value)[::-1] else False

    result = 0
    for num_a in range(999, 100, -1):
        for num_b in range(999, 100, -1):
            value_test = num_a * num_b
            if _is_palindrome(value_test) and value_test > result:
                result = value_test

    return result
