def gen():
    for character in 'AB':
        yield character
    for i in range(1,3):
        yield i

print('generator using for loops :')
print(">>> ",list(gen()))

def gen2():
    yield from 'AB'
    yield from range(1,3)

print('generator using yield from :')
print('>>> ', list(gen2()))