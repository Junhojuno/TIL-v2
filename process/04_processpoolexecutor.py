"""
Section 2
Parallelism with MultiProcessing > multiprocessing(3) : ProcessPoolExecutor
keyword : ProcessPoolExecutor, as_completed. futures, timeout, dict
"""
from concurrent.futures import ProcessPoolExecutor, as_completed
from urllib import request
from pprint import pprint as print


# 조회 URLs
URLs = [
    'http://www.daum.net/',
    'http://www.cnn.com/',
    'http://naver.com',
    'http://ruliweb.com',
    'https://www.google.co.kr/'
]

# 실행 함수
def load_url(url, timeout):
    with request.urlopen(url, timeout=timeout) as conn:
        return conn.read() # 페이지 소스


def main():
    # process pool context 영역
    with ProcessPoolExecutor(max_workers=5) as executor:
        # future 로드(실행x, 예약o)
        future_to_url = {executor.submit(load_url, url, 60) : url for url in URLs}
        
        # # 중간확인
        # print(future_to_url)
        
        # 실행
        for future in as_completed(future_to_url):
            # key값이 future 객체
            url = future_to_url[future]
            
            try:
                # 결과
                data = future.result()
            
            except Exception as e:
                # 예외처리
                print('%r generated an exception : %s' % (url, e))
            
            else:
                print('%r page is %d bytes' % (url, len(data)))



if __name__ == '__main__':
    main()
