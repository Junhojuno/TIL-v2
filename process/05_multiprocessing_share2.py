"""
Section 2
Parallelism with MultiProcessing > multiprocessing(4) : Sharing state
keyword : Memory sharing, array, value
"""
from multiprocessing import Process, current_process, Value, Array
import os

# 프로세스 메모리 공유 예제(공유가 되는 패턴)
def generate_update_number(v:int):
    for _ in range(50):
        v.value += 1
        
    print(f'process ID : {current_process().name}, data : {v.value}')
    

def main():
    # 부모 프로세스 ID
    parent_process_id = os.getpid()
    print(f'Parent process ID : {parent_process_id}')
    
    # 프로세스 리스트 선언
    processes = list()
    
    # 프로세스 메모리 공유 변수
    # share_numbers = Array('i', range(50)) # 리스트 등 공유 -> Array
    # from multiprocessing import shared_memory # 사용 가능(비교적 최근 파이썬 버전부터)
    # from multiprocessing import Manager # 사용 가능
    share_value = Value('i', 0) # 단일 변수 공유 -> Value
    
    for _ in range(1, 10):
        p = Process(target=generate_update_number, args=(share_value,))
        
        # 리스트에 담기
        processes.append(p)
        
        # 실행
        p.start()
        
    # join
    for p in processes:
        p.join()

    # share value가 정말로 공유되었는지 확인
    print(f'shared value : {share_value.value}')


if __name__ == '__main__':
    main()