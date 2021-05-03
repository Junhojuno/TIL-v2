"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : I/O Bound(5) > threading vs. multiprocessing vs. asyncio
keywords : I/O Bound, requests, asyncio
"""
import asyncio
import aiohttp
import time
from pprint import pprint as print

# I/O Bound AsyncIO 예제
# threading보다는 높은 코드 복잡도를 가짐(외부 lib이 비동기인지 확인, async/await을 붙여야 하는 등)
# 본 코드에서 requests는 동기 함수이므로 별도의 패키지 설치가 필요함

# 실행 함수1(다운로드)
async def request_site(url, session):
    # session 확인
    print(f'Session : {session}')
    
    async with session.get(url) as response:
        print(f'Read Contents :{response.content_length}, Status Code : {response.status}, from {url}')


async def request_all_sites(urls):
    async with aiohttp.ClientSession() as session: # with문은 async 붙여준다.
        # 작업 목록
        tasks = list()
        for url in urls:
            # task 목록 생성
            task = asyncio.ensure_future(request_site(url, session))
            tasks.append(task)
            
        # tasks 확인
        # print(*tasks)
        
        await asyncio.gather(*tasks, return_exceptions=True)


def main():
    # test URLs
    urls = ['https://www.jython.org',
            'http://olympus.realpython.org/dice',
            'https://realpython.com'] * 5
    
    # 실행시간 측정
    start_time = time.time()
    
    asyncio.run(request_all_sites(urls))
    # asyncio.get_event_loop().run_until_complete(request_all_sites(urls))
    
    
    # 실행시간 종료
    duration = time.time() - start_time
    
    # 결과 출력
    print(f'Downloaded {len(urls)} sites in {duration} seconds')


# 메인 영역
if __name__ == '__main__':
    main()
