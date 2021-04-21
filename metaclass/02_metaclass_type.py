"""

Meta Class(2)
keyword : Type(name, base, dict), Dynamic Meta Class

"""
"""

Meta Class
1. 메타 클래스 동적 생성
2. 동적 생성한 메타 클래스를 통해 커스텀 메타 클래스 생성 
3. 의도하는 방향으로 직접 클래스 생성에 관여할 수 있는 것이 장점

"""

# type 동적 클래스 생성
# Name(이름), Bases(상속되는 클래스 여부), Dict(속성/attributes, 메소드)

s1 = type('sample1', (), {}) # 클래스 동적 생성

print('what is s1 : ', s1)
print('type of s1 : ', type(s1))
print('base of s1 : ', s1.__base__)
print()

# type 동적 클래스 생성 + 상속
class Parent1:
    pass


s2 = type('Sample2', (Parent1,), dict(attr1=100, attr2='hi'))

print('what is s2 : ', s2)
print('type of s2 : ', type(s2))
print('base of s2 : ', s2.__base__)
print('s2 attributes : {} & {}'.format(s2.attr1, s2.attr2))
print()

# type 동적 클래스 생성 + 메소드

s3 = type('Sample3', 
          (), 
          {'attr1' : 300, 'attr2' : 100, 'add' : lambda x, y : x + y, 'mul' : lambda x, y : x * y})

print('what is s3 : ', s3)
print('type of s3 : ', type(s3))
print('base of s3 : ', s3.__base__)
print('s3 attributes : {} & {}'.format(s3.attr1, s3.attr2))
print('s3 attributes add : ', s3.add(s3.attr1, s3.attr2))
print('s3 attributes mul : ', s3.mul(s3.attr1, s3.attr2))
print()