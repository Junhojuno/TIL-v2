"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : I/O Bound(2) > threading vs. multiprocessing vs. asyncio
keywords : I/O Bound, requests, threading
"""
from concurrent import futures
import threading
import requests
import time

# I/O Bound Threading 예제

# 각 스레드에 생성되는 객체(독립된 네임스페이스 할당)
thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
        
    return thread_local.session


# 실행 함수1(다운로드)
def request_site(url):
    # session 획득
    session = get_session()
    
    # # session 확인
    print(f'session : {session}')
    # print(f'session header : {session.headers}')
    
    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}')


def request_all_sites(urls):
    # 멀티스레드 실행
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(request_site, urls)


def main():
    # test URLs
    urls = ['https://www.jython.org',
            'http://olympus.realpython.org/dice',
            'https://realpython.com'] * 5
    
    # 실행시간 측정
    start_time = time.time()
    
    request_all_sites(urls)
    
    
    # 실행시간 종료
    duration = time.time() - start_time
    
    # 결과 출력
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


# 메인 영역
if __name__ == '__main__':
    main()
