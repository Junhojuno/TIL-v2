"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : CPU Bound(2) > MultiProcessing
keywords : CPU Bound
"""
# CPU Bound 예제 MultiProcessing : 계산
import os
import time
from multiprocessing import current_process, Array, Manager, Process, freeze_support


# 실행함수 : 계산
def cpu_bound(number, total_list):
    process_id = os.getpid()
    process_name = current_process().name
    
    # 프로세스 정보 출력
    print(f'Process ID : {process_id}, Process Name : {process_name}')    
    total_list.append(sum(i ** 2 for i in range(number))) 


def main():
    numbers = [3_000_000 + x for x in range(30)]

    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 공유 매니저
    manager = Manager()
    
    # 리스트 획득(프로세스 공유)
    total_list = manager.list()

    # 실행시간 측정
    start_time = time.time()
    
    # 프로세스 생성 및 실행
    for i in numbers: # 1~100까지 적절히 조절
        # 생성
        p = Process(name=str(i), target=cpu_bound, args=(i, total_list,))
        
        # 배열에 담기
        processes.append(p)
        
        p.start()
        
    # join
    for process in processes:
        process.join()    
        
    # 결과 출력
    print(f'total list : {total_list}')
    print(f'Sum : {sum(total_list)}')
    
    # 실행 시간 종료
    duration = time.time() - start_time
    
    # 수행시간
    print(f'Duration : {duration} seconds')


if __name__ == '__main__':
    main()