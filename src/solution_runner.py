from __future__ import absolute_import, print_function, division

from _core import euler_solution

import problems
from problems import *

if __name__ == "__main__":
    for idx in range(len(problems.__all__)):
        result = None
        exec(f"result = problem_{idx+1}.solution()", globals(), result)
        euler_solution(result, idx+1)
