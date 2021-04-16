"""
Section 3
Concurrency, CPU Bound vs. I/O Bound : Blocking vs. Non-Blocking I/O
keywords : Blocking I/O, Non-Blocking I/O, Sync, Async
"""
"""
Blocking I/O vs. Non-Blocking I/O

    Blocking I/O
        - 시스템 콜 요청시(request) 커널에서 I/O 작업이 완료될때까지 응답 대기
        - 제어권 : I/O 작업 -> 커널이 소유 -> 응답(Response)전까지 대기(Block) -> 다른 작업 수행 불가(대기)
    
    Non-Blocking I/O
        - 시스템 콜 요청시, 커널에서 I/O 작업 완료여부에 상관없이 즉시 응답
        - 제어권 : I/O 작업 -> 유저 프로세스 -> 다른 작업 수행가능(지속) ---> 주기적으로 시스템 콜을 통해 I/O 작업의 완료 여부를 확인
        
    Sync vs. Async
        - Sync : I/O 작업 완료여부에 대한 noty는 유저 프로세스(호출하는 함수) -> 커널(호출되는 함수)
            -> 유저 프로세스에서 작업 완료여부를 계속 커널에 물어봄
        - Async : I/O 작업의 완료여부에 대한 noty는 커널(호출되는 함수) -> 유저 프로세스(호출하는 함수)
            -> 유저 프로세스는 다른 작업하고, 커널이 작업 완료여부를 알려줌
    
"""