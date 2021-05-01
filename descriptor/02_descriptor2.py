"""
Descriptor(2)
keyword : descriptor vs. property, low-level(descriptor) vs. high-level(property)

"""
"""
Descriptor
    1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
    2. property와 달리 재사용 가능
    3. ORM Framework 사용
"""

# Descriptor Example 2

import os
import logging


logging.basicConfig(format='%(asctime)s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')


class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value
        
    def __get__(self, obj, objtype=None):
        logging.info('Accessing %r giving %r', 'score', self.value)
        return self.value
    
    def __set__(self, obj, value):
        logging.info('Updating %r giving %r', 'score', self.value)
        self.value = value


class Student:
    # Descriptor instance
    score = LoggedScoreAccess()
    
    def __init__(self, name):
        # Regular instance attribute
        self.name = name

    

if __name__ == '__main__':
    s1 = Student('Juno')
    s2 = Student('Kate')
    
    # check score
    print(s1.score)
    
    # change the value.
    # get, set methods are called.
    s1.score += 20
    
    print(s1.score)
    print()
    
    # check score
    # share the value of score with instance 's1'
    print(s2.score)
    
    # change the value.
    # get, set methods are called.
    s2.score += 200
    
    print(s2.score)
    print(s1.score)
    
    # check __dict__
    print('vars(s1) : ', vars(s1))
    print('vars(s2) : ', vars(s2))
    print('s1.__dict__ : ', s1.__dict__)
    print('s2.__dict__ : ', s2.__dict__)