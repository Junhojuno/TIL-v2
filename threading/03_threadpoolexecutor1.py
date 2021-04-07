"""
Python Lever 4(thread chapter)

Section 1
Multithreading - Thread(3) - ThreadPoolExecutor
keyword : Many Threads, concurrent.futures, (xxx)PoolExecutor
"""
"""
그룹 스레드
(1) python 3.2 이상 표준 라이브러리에서 사용가능
(2) concurrent.futures
(3) with 사용으로 thread 생성, 소멸 등의 라이프사이클 관리 용이
(4) 디버깅하기가 난해함(단점)
(5) 대기중인 작업 -> 내부적으로 Queue에 담김 -> 완료 상태 조사 -> 결과 또는 예외를 받아옴 -> 단일화(캡슐화)

"""
import logging
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    logging.info("Sub-Thread %s starting", name)
    
    result = 0
    for i in range(10001):
        result += i
        
    logging.info("Sub-Thread %s finishing result %d", name, result)

    return result
    

def main():
    # logging format
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main Thread : before creating and running thread")

    # # 실행 방법 1 -> task의 수가 늘어나면 코드라인이 늘어남
    # # max_workers : 작업의 개수가 넘어가면 직접 설정하는 것이 유리함...(???)
    # executor = ThreadPoolExecutor(max_workers=3)
    # task1 = executor.submit(task, ('first',))
    # task2 = executor.submit(task, ('second',))

    # # 결과값 있을 경우
    # print(task1.result())
    # print(task2.result())

    # 실행 방법 2
    with ThreadPoolExecutor(max_workers=3) as executor:
        tasks = executor.map(task, ['first', 'second'])
        
        # 결과 확인
        print(tasks) # iterator
        print(list(tasks))

if __name__ == '__main__':
    main()

