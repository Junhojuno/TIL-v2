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

# Property 클래스를 사용하여 Descriptor 직접 구현
# magic method가 아닌 자유롭게 method 설정 가능
# class property(fget=None, fset=None, fdel=None, doc=None)

class DescriptorEx2:
    
    def __init__(self, value):
        self._name = value
        
    def get_value(self):
        return f'Get method is called -> self : {self}, name : {self._name}'
    
    def set_value(self, value):
        print('Set method is called.')
        
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('Name should be string.')
        
    def del_value(self):
        print('Del method is called.')
        self._name = None
        
    name = property(fget=get_value, fset=set_value, fdel=del_value, doc='Property Method Example')

    

if __name__ == '__main__':
    s2 = DescriptorEx2('Descriptor Test 2')
    
    # 최초값 확인
    print(s2.name)
    
    # set_value 호출
    s2.name = 'Descriptor Test2 Method'
    
    # get_value 호출
    print(s2.name)
    
    # del_value 호출
    del s2.name
    
    # doc 확인
    print(DescriptorEx2.name.__doc__)
    
    # 예외 발생
    s2.name = 10101