"""
Problem 2:

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.
"""

from __future__ import absolute_import, print_function, division


def solution(max_range: int = 4000000) -> int:
    result = 0
    prev_term = 0
    term = 1
    while term < max_range:
        current = term
        term = prev_term + term
        prev_term = current
        if term % 2 == 0:
            result += term

    return result
