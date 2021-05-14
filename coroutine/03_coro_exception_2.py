class DemoException(Exception):
    """exception using in averager """

def demo_finally():
    print(">>> coroutine started")
    try:
        while True:
            try:
                x = yield
                # print(">>> coroutine received : {!r}".format(x))
            except DemoException:
                print("*** DemoException handled. Continuing...")
            else:
                print(">>> coroutine received : {!r}".format(x))
    finally:
        print(">>> coroutine end up.")


from inspect import getgeneratorstate
print('='*30)
exc_coro = demo_finally()
print(next(exc_coro))
print(exc_coro.send(11))
exc_coro.throw(ZeroDivisionError) # 처리 못함
print(exc_coro.send(22))
getgeneratorstate(exc_coro)
print('='*30)
print()