"""
Logging : 이벤트 로깅

장점
    - 모든 파이썬 모듈이 로깅에 참여할 수 있어서, 응용 프로그램 로그에 여러분 자신의 메시지를 제삼자 모듈의 메시지와 통합할 수 있다는 것
        = ???
        
구성요소
    - Logger : expose the interface that application code directly uses. = ???
    - Handler : logger로부터 생성된 log기록을 적절한 목적지에 보내는 역할.
        -> StreamHandler :  
    - Filter : 출력할 log기록을 결정하기위한 세부적인 기능 제공하는 역할.
    - Formatter : 최종 출력에서 log기록의 전반적인 레이아웃을 정하는 역할.

"""