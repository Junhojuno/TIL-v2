from collections import namedtuple

# 평균을 계산하는 코루틴 함수가 반환하는 결과를 namedtuple로 반환
Result = namedtuple('Result', 'count average')

def averager():
    average = None
    total = 0.0
    count = 0
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

coro_avg = averager()
print(next(coro_avg))
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(6.5))
try:
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value
print(result)