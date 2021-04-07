"""
Section 2
Parallelism with MultiProcessing : Process vs. Thread
keyword : Process, Thread, Parallelism
"""
"""
(1) Parallelism
    - 완전히 동일한 타이밍(시점)에 task를 실행
    - 다양한 파트로 나눠서 실행
    - MultiProcessing에서 cpu가 1 core인 경우는 만족하지 않음.
    
(2) Process vs. Thread(차이 비교)
    - 독립된 메모리(process), 공유 메모리(Thread)
    - 많은 메모리 필요(process), 적은 메모리(Thread)
    - 좀비(데드) 프로세스 생성 가능성 높음, 좀비(데드) 스레드 생성 가능성은 상대적으로 낮음
    - 오버헤드 큼(process), 오버헤드 작음(Thread)
    - 생성/소멸이 다소 느림(process), 상대적으로 생성/소멸이 빠름(Thread)
    - 코드 작성이 쉬움 but 디버깅은 어려움(process), 코드 작성이 어려움 & 디버깅도 어려움(Thread)

"""