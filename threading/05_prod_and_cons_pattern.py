"""
Python Lever 4(thread chapter)

Section 1
Multithreading - Thread(5) - Prod vs. Cons using Queue
keyword : 생산자-소비자 패턴(Producer-Consumer Pattern)
"""
"""
Producer-Consumer Pattern
(1) MultiThread/MultiProcessing 디자인 패턴의 정석
(2) 서버측 프로그래밍의 핵심
    -> (Producer) 영상 촬영 또는 영상 데이터 수집
    -> (Consumer) 영상 데이터 DB 저장 및 활용
(3) 주로 허리역할을 하기때문에 중요함

Python Event 객체
(1) Flag : 초기값(0)
(2) 다음의 형태로 Flag값 변경
    - Set() -> 1
    - Clear() -> 0
    - Wait
        1 -> return, 
        0 -> 대기
    - isSet() -> 현재 Flag 상태 반환

"""
from concurrent import futures
import logging
import queue
import random
import threading
import time


# 생산자
def producer(queue, event):
    """
    네트워크 대기 상태라 가정(서버)
    """
    while not event.is_set(): # event flag 값이 0이라면
        message = random.randint(1, 11)
        logging.info('producer makes message : %s', message)
        queue.put(message)
        
    logging.info('producer receive Exit event')


# 소비자
def consumer(queue, event):
    """
    응답 받고 소비하는 것으로 가정 or DB 저장
    """
    while not event.is_set() or not queue.empty():
        message = queue.get() # 선입선출
        logging.info('consumer got a message : %s (size=%d)', message, queue.qsize())
        
    logging.info('consumer receive Exit event')
    



if __name__ == '__main__':
    # Logging format
    format = '%(asctime)s : %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    
    # queue 지정, 사이즈가 중요
    pipeline = queue.Queue(maxsize=10)
    
    # 이벤트 flag 초기값 0
    event = threading.Event()
    
    # with context
    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        
        # 실행시간 조정, 보통 while문
        time.sleep(0.1)
        
        logging.info('Main : about to set event')
        
        # 프로그램 종료
        event.set()
        
    
