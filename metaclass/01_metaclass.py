"""

Meta Class(1)
keyword : class of class, Type, Meta class, Custom Meta class

"""
"""

Why Meta Class?
1. 클래스를 만드는 역할, 의도하는 방향으로 클래스를 customize
2. 프레임워크 작성 시 필수
3. Type 함수가 동적 생성, 커스텀 생성을 가능하게 함
4. 검증 클래스 등 커스텀 클래스 구성/설계 가능
5. 엄격한 클래스 사용 요구, 메소드 오버라이딩 요구 등

"""

# type 예제
class SampleA:
    pass


obj1 = SampleA()

print(f'obj1 class : {obj1.__class__}') # <class '__main__.SampleA'>
print(f'obj1 class using type function : {type(obj1)}') # <class '__main__.SampleA'>
print('Above results are same, right? ', obj1.__class__ is type(obj1))

print(f'what is class of class : {obj1.__class__.__class__}') # <class 'type'>

# type 클래스와 같은 메타 클래스에 변수/메소드 추가를 하면 하위 클래스는 광범위하게 적용받게 됨 -> 동적으로 변화 가능

print('what is type class\'s meta class ? ', type.__class__)
