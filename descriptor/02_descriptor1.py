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

# Descriptor Example 1

import os


class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))


class DirectoryPath:
    # Descriptor instance
    size = DirectoryFileCount()
    
    def __init__(self, dirname):
        self.dirname = dirname
    

if __name__ == '__main__':
    path = DirectoryPath('./')
    print(path.size)