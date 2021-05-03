"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : I/O Bound(4) > AsyncIO basic
keywords : asyncio
"""
"""
AsyncIO : I/O Bound에서의 Non-Blocking 비동기 프로그래밍
    - 파이썬 3.4에서 비동기 표준라이브러리로 등장함
    - 일반적인 함수(def)는 동기(sync)로 작동함 -> async def로 선언함으로써 비동기화 시켜주면 됨
    - 비동기 함수안에서 다른 비동기 함수를 호출할때는 호출되는 비동기 함수앞에 `await`을 붙여줘야 함


"""
import time
import asyncio


def exe_calculate_sync(name, n):
    for i in range(1, n+1):
        print(f'{name} -> {i} of {n} is calculating....')
        time.sleep(1)
        
    print(f'{name} - {n} working done!')


def process_sync():
    start = time.time()
    
    exe_calculate_sync('one', 1)
    exe_calculate_sync('two', 2)
    exe_calculate_sync('three', 3)
    
    end = time.time()

    print(f'>>>> total seconds : {end - start}')


async def exe_calculate_async(name, n):
    for i in range(1, n+1):
        print(f'{name} -> {i} of {n} is calculating....')
        # time.sleep(1) -> 동기 함수
        await asyncio.sleep(1)
        
    print(f'{name} - {n} working done!')
    

async def process_async():
    start = time.time()
    
    await asyncio.wait([exe_calculate_async('one', 1),
                        exe_calculate_async('two', 2),
                        exe_calculate_async('three', 3)
                        ])
    
    
    end = time.time()

    print(f'>>>> total seconds : {end - start}')


# 메인 영역
if __name__ == '__main__':
    # # Sync 실행
    # process_sync()

    # Async 실행
    # Python 3.7 이상
    asyncio.run(process_async())
    
    # # Python 3.7 이하
    # asyncio.get_event_loop().run_until_complete(process_async())
