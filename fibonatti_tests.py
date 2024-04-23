from functools import wraps, lru_cache
from time import perf_counter
from sys import setrecursionlimit
from memory_profiler import profile
import logging

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f'{func.__name__} ran in {end - start:.4f}s')
        return result
    return wrapper

logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def debug_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args {args} and kwargs {kwargs}')
        logging.info(f'Calling {func.__name__} with args {args} and kwargs {kwargs}')
        return func(*args, **kwargs)
    return wrapper
        
@lru_cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

@debug_log
@timer
@profile
def main():
    r = 30
    for i in range(r):
        print(fib(i))

if __name__ == '__main__':
    setrecursionlimit(10000)
    main()