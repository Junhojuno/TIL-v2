"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : I/O Bound(1) > Synchronous
keywords : I/O Bound, requests
"""
import requests
import time


# 실행 함수1(다운로드)
def request_site(url, session):
    # print(f'session : {session}')
    # print(f'session header : {session.headers}')
    
    with session.get(url) as response:
        print(f'[Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}')


def request_all_sites(urls):
    with requests.Session() as session:
        for url in urls:
            request_site(url, session)


def main():
    # test URLs
    urls = ['https://www.jython.org',
            'http://olympus.realpython.org/dice',
            'https://realpython.com'] * 3
    
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
