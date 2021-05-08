# coroutine을 활용한 이동평균 계산 함수 -> 클로저를 활용한 이동평균 계산 함수와 비교
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count


if __name__ == '__main__':
    coroutine_avg = averager()
    v1 = next(coroutine_avg)
    print(v1) # None
    v2 = coroutine_avg.send(10) 
    print(v2) # 10 
    v3 = coroutine_avg.send(30)
    print(v3) # 20
    v4 = coroutine_avg.send(5)
    print(v4) # 15