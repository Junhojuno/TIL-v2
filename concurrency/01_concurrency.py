"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : What is Concurrency?
keywords : Concurrency
"""
"""
동시성(Concurrency)
    - CPU 가용성을 극대화하기 위해, 병렬성(Parallelism)의 단점/어려움을 S/W(구현) 레벨에서 해결하기위한 방법
    - 싱글코어에서 MultiThread 패턴으로 작업처리하는 것이 대표적인 예
    - 동시 작업에 있어서 일정량을 처리하고 다음 작업으로 넘기는 방식(이전 작업은 다음에 **이어서** 마무리)
    - 즉, 제어권을 주고 받으며 작업을 처리하는 패턴
    - 병렬적이지는 않지만 유사한 처리 방식
    
동시성(Concurrency) vs. 병렬성(Parallelism)
    - 동시성 : 논리적, 동시 실행 패턴, 싱글/멀티 코어에서 실행가능, 하나의 작업을 공유하며 처리하는 패턴
        -> 디버깅이 굉장히 어려움(mutex, dead lock)
    
    - 병렬성 : 물리적으로 동시 실행(H/W적인 느낌), 멀티 코어에서 구현가능, 주로 별개의 작업처리
        -> 이것도 디버깅이 어려움
    
"""