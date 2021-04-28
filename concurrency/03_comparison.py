"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : MultiProcessing vs. Threading vs. AsyncIO
keywords : CPU Bound, I/O Bound, AsyncIO
"""
"""
CPU Bound vs. I/O Bound
    
    CPU Bound
        - 프로세스 진행이 CPU 속도에 의해 결정됨 -> 행렬 곱, 고속 연산, 압축 파일 등
        - CPU 연산 위주의 작업 수행
        
    I/O Bound
        - 파일 쓰기, 디스크 작업, 네트워크 통신, 시리얼 포트 송수신 -> 작업에 의해 작업수행시간이 결정됨(병목현상)
        - CPU 성능 지표가 수행시간 단축에 크게 영향을 끼치지 않음

메모리 바인딩, 캐시 바운딩

작업 목적에 따라서 적절한 동시성 라이브러리 선택이 중요함

최종 비교

    1. MultiProcessing : Multiple Processes, 고가용성 CPU utilization(CPU Bound) -> 10개의 부엌, 10명의 요리사, 10개의 요리
    2. Threading : Single Thread/Process, Multiple Threads, OS가 작업 스위칭을 결정함(Fast I/O Bound) -> 1개의 부엌, 10명의 요리사, 10개의 요리
    3. AsyncIO : single Process/Thread, cooperative multitasking, tasks cooperatively decide switching(Slow I/O Bound) -> 1개 부엌, 1명의 요리사, 10개의 요리

"""