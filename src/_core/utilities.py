from __future__ import absolute_import, print_function, division

import math


def euler_solution(solution, problem_num: int):
    """
    Formats the solution in a clean manner
    :param solution: value of the problem
    :param int problem_num: Project Euler problem number
    """
    url = f"https://projecteuler.net/problem={problem_num}"
    print(f"Problem {problem_num} solution: {solution} | {url}")


def generate_primes(limit: int = 20) -> list:
    primes = [2]
    for value in range(3, limit, 2):
        step = 0
        is_prime = True
        while primes[step] ** 2 <= value:
            if value % primes[step] == 0:
                is_prime = False
                break
            step += 1

        if is_prime:
            primes.append(value)

    return primes
