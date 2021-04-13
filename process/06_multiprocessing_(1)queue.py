"""
Section 2
Parallelism with MultiProcessing > multiprocessing(5) : Queue, Pipe
keyword : queue, pipe, Communication between processes
"""
from multiprocessing import Process, Queue, current_process
from multiprocessing.process import parent_process
import time
import os

# 프로세스 통신 구현 : Queue

# 실행함수
def worker(id, baseNum, q):
    process_id = os.getpid()
    process_name = current_process().name
    
    # 누적
    sub_total = 0
    
    # 계산
    for i in range(baseNum):
        sub_total += 1
        
    # produce
    q.put(sub_total)
    
    # 정보 출력
    print(f'Process ID : {process_id}, Process name : {process_name}, ID : {id}')
    print(f'Result : {sub_total}')


def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f'Parent Process ID : {parent_process_id}')
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 시작 시간
    start_time = time.time()
    
    # Queue 선언
    q = Queue()
    
    for i in range(5):
        # 생성
        p = Process(name=str(i), target=worker, args=(i, 100000000, q))
        
        # 리스트에 담기
        processes.append(p)
        
        # 시작
        p.start()
        
    # Join
    for process in processes:
        process.join()
        
    # 순수 계산 시간
    print('---- %s seconds ----' % (time.time() - start_time))
    
    # 종료 플래그
    q.put('exit')
    
    # 대기
    total = 0
    while True:
        tmp = q.get()
        if tmp == 'exit':
            break
        else:
            total += tmp
            
    print()
    print(f'Main-Processing Total count = {total}')
    print('Main-Process is done!')



if __name__ == '__main__':
    main()