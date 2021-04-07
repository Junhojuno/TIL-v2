"""
Python Lever 4(thread chapter)

Section 1
Multithreading - Thread(4) - Lock, DeadLock
keyword : Lock, DeadLock, Race condition, Thread Synchronization
"""
"""
용어 설명
(1) 세마포어(Semaphore) : 프로세스간 공유된 자원에 접근 시, 문제 발생 가능성이 있음
    -> 한 개의 프로세스만 접근 처리하도록 고안(경쟁 상태 예방)
    -> (머릿속으로 그림그리기)여러 화장실, 그것보다 많은 대기인원

(2) 뮤텍스(Mutex) : 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것 
    -> 이 또한, 경쟁 상태 예방 목적
    -> (머릿속으로 그림그리기)하나의 화장실, 대기인원 여러명
    
(3) Lock : 상호 배제를 위한 잠금(lock) 처리 -> 데이터 경쟁이라고도 볼 수 있음.

(4) 데드락(DeadLock) : 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착 상태)

(5) 스레드 동기화(Thread Synchronization) : 교착 상태등을 해결함으로써 안정적으로 동작하게 처리한다(동기화 메소드, 동기화 블록)
(6) Semaphore vs. Mutex : 
    -> 세마포어와 뮤텍스 개체는 모두 병렬 프로그래밍 환경에서 상호배제를 위해 사용됨
    -> 뮤텍스 개체는 단일 스레드가 리소스 또는 중요 섹션 소비를 허용
    -> 세마포어는 리소스에 대한 제한된 수의 동시 엑세스(access)를 허용
    -> 화장실 갯수로 생각해볼것(각각 프로세스와 스레드에 대한 개념이 담겨져 있다는 점)

"""
import logging
from concurrent.futures import ThreadPoolExecutor
import time
import threading


class FakeDataStore: # 스레드간 공유되는 code가 클래스의 전반적인 코드라고 볼 수 있음...(???)
    # 공유 변수(value) -> 스레드간 공유되는 data, heap 영역
    def __init__(self):
        self.value = 0 # -> 맨 아래 메인 스레드에서 호출가능해야하기 때문에 공유되는 영역(data, heap)에 있어야 함.
        self._lock = threading.Lock()
    
    # 변수 업데이트 함수
    def update(self, n): # -> 자기만의(객체별) stack 영역
        logging.info("Thread %s : Starting update", n)
        
        # 뮤텍스 or lock 등 thread synchronization이 필요한 곳
        
        # # lock 획득(방법1) -> 사용중엔 열쇠로 잠궈버리겠다.
        # self._lock.acquire()
        # logging.info("Thread %s has lock", n)
        
        # local_copy = self.value 
        # local_copy += 1
        # time.sleep(0.1)
        # self.value = local_copy
        
        # logging.info("Thread %s about to release lock", n)
        
        # # lock 반환
        # self._lock.release()
        
        # lock 획득(방법2)
        with self._lock:
            logging.info("Thread %s has lock", n)
        
            local_copy = self.value 
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            
            logging.info("Thread %s about to release lock", n)
        
        
        logging.info("Thread %s : finishing update", n)
        

if __name__ == '__main__':
    # logging format
    format = "%(asctime)s : %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 클래스 인스턴스화
    store = FakeDataStore()
    
    logging.info("Testing update. Starting value is %d", store.value)
    
    # with context
    with ThreadPoolExecutor(2) as executor:
        for n in ['first', 'second', 'third']:
            executor.submit(store.update, n) 
            
    logging.info("Testing update. Starting value is %d", store.value) # 3이 나와야 할 거 같지만, 2가 나옴(race condition)

