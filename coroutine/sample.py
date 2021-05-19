def main_generator():
    value = yield from sub_generator(1)

def sub_generator(x):
    print('sub_generator start : ', x)
    y = yield x
    print('sub_generator middle : ', y)
    z = yield x + y
    print('sub_generator last : ', z)

def main():
    """caller"""
    pass

sub_gen = sub_generator(10)
value = next(sub_gen) # priming
print(value)
# value = sub_gen.send(10)
# print(value)
# sub_gen.send(10)
