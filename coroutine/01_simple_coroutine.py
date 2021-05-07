def simple_coroutine():
    print('>>> coroutine started')
    print('>>> something is between here')
    x = yield
    print('>>> coroutine received : ', x)

my_coro = simple_coroutine()
# print(my_coro) # generator object
print(next(my_coro))
# my_coro.send(42)