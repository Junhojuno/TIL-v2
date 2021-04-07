"""
Python Lever 4(thread chapter)

Section 1
Multithreading - Thread(2) - Daemon, Join
keyword : DaemonThread, Join
"""
"""
DaemonThread(데몬스레드)
(1) 백그라운드에서 실행
(2) 메인스레드 종료시 즉시 종료
(3) 주로 백그라운드 무한 대기 이벤트 발생을 실행하는 부분 담당(보조의 역할) -> ex) JVM(garbage collection), 자동 저장 기능
(4) 일반 스레드는 작업 종료시까지 실행(메인 스레드가 끝나던지 말던지)

"""

import logging
import threading
import time


def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)
    
    for i in d:
        print(i)
        
    logging.info("Sub-Thread %s: finishing", name)


# 메인 영역(main thread) : main thread의 흐름을 타는 시작점()
if __name__ == '__main__':
    # logging format
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread : before creating thread")
    
    # 함수 인자 확인
    # Daemon -> default : False
    x = threading.Thread(target=thread_func, args=('first', range(20000)), daemon=True)
    y = threading.Thread(target=thread_func, args=('second',range(10000)), daemon=True)

    logging.info("Main-Thread : before running thread")
    
    # 서브 스레드 시작
    x.start()
    y.start()
    
    # DaemonThread 여부 확인
    print(x.isDaemon())
    print(y.isDaemon())
    
    # # 주석 전후 결과 확인
    # x.join() # 서브 스레드의 작업이 끝날때까지 메인 스레드는 기다리도록 한다.
    # y.join()
    
    logging.info("Main-Thread : waiting for the thread to finish")
    
    logging.info("Main-Thread : all done")