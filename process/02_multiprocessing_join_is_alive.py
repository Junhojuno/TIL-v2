"""
Section 2
Parallelism with MultiProcessing > multiprocessing(1) : Join, is_alive
keyword : multiprocessing, processing state
"""
from multiprocessing import Process, process
import time
import logging


def process_func(name):
    print(f'sub-process {name} : starting')
    time.sleep(3)
    print(f'sub-process {name} : finishing')


def main():
    # logging format
    format = '%(asctime)s : %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')

    # 함수 인자 확인
    p = Process(target=process_func, args=('first',))
    
    logging.info('Main-Process : before creating Process')
    
    # 프로세스
    p.start()
    
    logging.info('Main-Process : During Process')
    
    # logging.info('Main-Process : Terminate Process')
    # p.terminate()
    
    logging.info('Main-Process : Joined Process')
    p.join()
    
    # 프로세스 상태 확인
    print(f'Process p is alive : {p.is_alive()}')


# 메인 시작
if __name__ == '__main__':
    main()
