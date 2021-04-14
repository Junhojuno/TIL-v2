"""
Section 2
Parallelism with MultiProcessing > multiprocessing(5) : Queue, Pipe
keyword : queue, pipe, Communication between processes
"""
from multiprocessing import Process, Pipe, current_process
from multiprocessing.process import parent_process
import time
import os

# 프로세스 통신 구현 : Pipe
# 부모-자식 프로세스간 1:1 연결

# 실행함수
def worker(id, baseNum, conn):
    process_id = os.getpid()
    process_name = current_process().name
    
    # 누적
    sub_total = 0
    
    # 계산
    for i in range(baseNum):
        sub_total += 1
        
    # produce
    conn.send(sub_total)
    conn.close()
    
    # 정보 출력
    print(f'Process ID : {process_id}, Process name : {process_name}, ID : {id}')
    print(f'Result : {sub_total}')


def main():
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f'Parent Process ID : {parent_process_id}')
    
    # 시작 시간
    start_time = time.time()
    
    # Pipe 선언
    parent_conn, child_conn = Pipe()
    
    # 생성
    p = Process(name='1', target=worker, args=(1, 100000000, child_conn))
    
    # 시작
    p.start()
        
    # Join
    p.join()
        
    # 순수 계산 시간
    print('---- %s seconds ----' % (time.time() - start_time))

    print()
    print(f'Main-Processing Total count = {parent_conn.recv()}')
    print('Main-Process is done!')



if __name__ == '__main__':
    main()