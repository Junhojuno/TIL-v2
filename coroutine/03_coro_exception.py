class DemoException(Exception):
    """예외 유형"""

# 처리된 예외(except DemoException 부분) 이외의 예외 발생시 무한루프가 중단됨.
def demo_exc_handling():
    print('>>> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing....')
        else: # 예외가 발생하지 않으면 받은 값을 출력한다.
            print('>>> coroutine received : {!r}'.format(x))

    raise RuntimeError('This line should never run.')

################# 예외를 발생시키지 않는 demo_exc_handling()의 활성화 및 종료 #################
print('='*30)
exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
print(exc_coro.send(22))
exc_coro.close()

from inspect import getgeneratorstate
print(getgeneratorstate(exc_coro))
print('='*30)
print()
#######################################################################################

################# DemoException을 demo_exc_handling()안에 던져도 종료되지 않는다(처리가능한 예외).#################
print('='*30)
exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
exc_coro.throw(DemoException)
getgeneratorstate(exc_coro)
print('='*30)
print()
##########################################################################################################

################ 예외를 처리할 수 없는 경우 ################
print('='*30)
exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
exc_coro.throw(ZeroDivisionError)
getgeneratorstate(exc_coro)
print('='*30)
#######################################################