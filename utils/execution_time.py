from timeit import default_timer


class Timer(object):
    def __enter__(self):
        self.start = default_timer()
        return self

    def __exit__(self, *args):
        self.end = default_timer()
        self.interval = self.end - self.start


def execution_time(loops=1, verbose=True):
    msg_loop = "[{func}]<loop: {loop}> execution time: {time} s"
    msg_avg = "[{func}] avg execution time: {time} s, loops: {loops}"

    avg = lambda result: sum(result)/len(result)

    def wrap(func):
        def inner(*args, **kwargs):
            results = []
            for index, loop in enumerate(range(0, loops)):
                with Timer() as timer:
                    func(*args, **kwargs)
                _time = timer.interval
                results.append(_time)
                if verbose:
                    print(msg_loop.format(
                        func=func.__name__, loop=index+1, time=_time))

            print(msg_avg.format(
                func=func.__name__, time=avg(results), loops=loops))
        return inner
    return wrap
