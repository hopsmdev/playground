import timeit
from timeit import default_timer as timer


def execution_time(func):
    def inner(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        end = timer()
        print("[{func}] execution time: {time} s".format(
            func=func.__name__, time=end - start))
    return inner