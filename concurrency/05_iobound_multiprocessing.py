"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : I/O Bound(3) > threading vs. multiprocessing vs. asyncio
keywords : I/O Bound, requests, MultiProcessing
"""
import multiprocessing
import requests
import time

# I/O Bound MultiProcessing 예제

# 각 프로세스 메모리 영역에 생성되는 객체(독립적)
# 함수 실행할 때마다 객체를 생성하는 것은 좋지 않음 -> 각 프로세스 마다 초기화하여 할당하자
session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()


# 실행 함수1(다운로드)
def request_site(url):
    # session 확인
    print(f'Session : {session}')
    
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f'[{name} -> Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}')


def request_all_sites(urls):
    # 멀티프로세스 실행
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool:
        pool.map(request_site, urls)


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
