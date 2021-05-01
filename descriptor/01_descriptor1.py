"""
Descriptor(1)
keyword : descriptor, set, get, del, property

"""
"""
Descriptor
    1. 객체에서 서로 다른 객체를 속성값으로 가지는 것.
    2. Read(=get), Write(=set), Delete(=del) 등을 미리 정의할 수 있음.
    3. data descriptor : set, del
    4. non-data descriptor : get
    5. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능
"""

class DescriptorEx1:
    
    def __init__(self, name='default'):
        self.name = name
        
    def __get__(self, obj, obj_type):
        return f'Get method is called -> self : {self}, obj : {obj}, obj_type : {obj_type}, name : {self.name}'
    
    def __set__(self, obj, name):
        print('Set method is called.')
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name should be string.')
        
    def __delete__(self, obj):
        print('Delete method is called.')
        self.name = None


class Sample1:
    """Descriptor를 사용하기 위한 별도의 클래스 정의 필요"""
    name = DescriptorEx1()
    

if __name__ == '__main__':
    s1 = Sample1()
    
    # set 호출
    s1.name = 'Descriptor Test 1'
    
    # 예외 발생
    # s1.name = 1000

    # get 호출
    print(s1.name)
    
    # del 호출
    del s1.name

    # 지워졌는지 다시 한 번 확인
    print(s1.name)
