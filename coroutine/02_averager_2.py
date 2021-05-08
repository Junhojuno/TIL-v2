from functools import wraps

def coroutine(func):
    """decorator for primining(기동) coroutine"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    average = None
    total = 0.0
    count = 0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

coro_avg = averager()
from inspect import getgeneratorstate
getgeneratorstate(coro_avg)
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))