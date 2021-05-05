"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : CPU Bound(1) > Synchronous
keywords : CPU Bound
"""
# CPU Bound 예제 : 계산
import time


# 실행함수 1 : 계산
def cpu_bound(number):
    return sum(i ** 2 for i in range(number))


# 실행함수 2
def find_sums(numbers):
    result = [cpu_bound(number) for number in numbers]
    return result


def main():
    numbers = [3_000_000 + x for x in range(30)]

    # 실행시간 측정
    start_time = time.time()
    
    # 실행
    total = find_sums(numbers)
    
    # 결과 출력
    print(f'total list : {total}')
    print(f'Sum : {sum(total)}')
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    # 수행시간
    print(f'Duration : {duration} seconds')


if __name__ == '__main__':
    main()