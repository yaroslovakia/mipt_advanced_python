#код не работает, но я не могу понять, почему

import time
import sys
import argparse
from functools import wraps

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('filename')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

filepath = namespace.filename

def decorator_file(filepath):
    def wrapper(function):
        def out(*args, **kwargs):
            start_time = time.perf_counter_ns()
            res = function(*args, **kwargs)
            with open("filepath", "w") as file:
                file.write(str(start_time))
            return res
        return out
    return wrapper


@decorator_file
def func(x):
    result = x*2
    print(result)
func(2)




