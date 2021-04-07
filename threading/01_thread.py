"""
Python Lever 4(thread chapter)

Section 1
Multithreading - Thread(1) - basic
keyword : Threading basic
"""
import logging
import threading
import time


def thread_func(name):
    logging.info("Sub-Thread %s: starting", name)
    time.sleep(3)
    logging.info("Sub-Thread %s: finishing", name)


# 메인 영역(main thread) : main thread의 흐름을 타는 시작점
if __name__ == '__main__':
    # logging format
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread : before creating thread")
    
    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('first',))

    logging.info("Main-Thread : before running thread")
    
    # 서브 스레드 시작
    x.start()
    
    # 주석 전후 결과 확인
    x.join() # 서브 스레드의 작업이 끝날때까지 메인 스레드는 기다리도록 한다.
    
    logging.info("Main-Thread : waiting for the thread to finish")
    
    logging.info("Main-Thread : all done")
