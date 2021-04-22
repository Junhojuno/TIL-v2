"""

Meta Class(3)
keyword : Type inheritance, Custom Meta Class

"""
"""

Meta Class Inheritance
1. type 클래스 상속
2. 메타 클래스 속성 사용
3. 커스텀 메타 클래스 생성
    - 클래스 생성 가로채기(intercept) --> type 상속 예제 속 __init__이나 __new__에서 dict 수정하는 등의 행위
    - 클래스 개선 및 수정하기(modify) --> List 상속 받아서 기능 추가하여 나만의 list 클래스 만드는 등
    - 수정된 클래스를 반환하는 기능
    
"""

# 커스텀 메타 클래스 생성 : type 상속 No

def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d
        

def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new
        
# list를 상속받고, 위의 두 메소드가 추가된 커스텀 메타 클래스 생성
CustomList1 = type('CustomList1', 
                   (list, ), 
                   {
                       'desc' : '커스텀 리스트 1', 
                       'cus_mul' : cus_mul, 
                       'cus_replace' : cus_replace
                       }
                   )

c1 = CustomList1([1,2,3,4,5,6,7]) # initialize
print('what is c1 : ', c1)
c1.cus_mul(10)
print('after multiplication, c1 : ', c1)
c1.cus_replace(10, 9999)
print('after replacement, c1 : ', c1)
print('c1 desc : ', c1.desc)


# 커스텀 메타 클래스 생성 : type 상속 Yes (위의 예제와 동일하게 동작하지만, 다른 구현 방식)
# class MetaClassName(type):
#     def __new__(metacls, name, bases, namespace):
#        code...

# __new__ -> __init__ -> __call__ 순서로 실해됨 
class CustomListMeta(type):
       
    def __init__(self, object_or_name, bases, dct):
        """__new__에서 생성된 인스턴스"""
        print('__init__ -> ', self, object_or_name, bases, dct)
        super().__init__(object_or_name, bases, dct)
    
    def __call__(self, *args, **kwargs):
        """인스턴스 실행"""
        print('__call__ -> ', self, *args, **kwargs)
        return super().__call__(*args, **kwargs)
    
    def __new__(metacls, name, bases, namespace):
        """클래스 인스턴스 생성(메모리 초기화)"""
        print('__new__ -> ', metacls, name, bases, namespace)
        namespace['desc'] = '커스텀 리스트2'
        namespace['cus_mul'] = cus_mul
        namespace['cus_replace'] = cus_replace
        
        return type.__new__(metacls, name, bases, namespace)
    
CustomList2 = CustomListMeta('CustomList2', (list, ), {})

c2 = CustomList2([1,2,3,4,5,6,7])
print('what is c2 : ', c2)
c2.cus_mul(100)
print('after multiplication, c2 : ', c2)
c2.cus_replace(100, -9999)
print('after replacement, c2 : ', c2)
print('c2 desc : ', c2.desc)