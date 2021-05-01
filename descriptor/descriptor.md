## Descriptor?
  1. 객체에서 서로 다른 객체를 속성값으로 가지는 것.
  2. Read(=get), Write(=set), Delete(=del) 등을 미리 정의할 수 있음.
  3. data descriptor : set, del
  4. non-data descriptor : get
  5. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로 생성 가능

### Descriptor 사용 예시(1) : 동적 조회
- [여기](https://docs.python.org/ko/3/howto/descriptor.html#dynamic-lookups)의 코드를 활용하였음
- 지속적으로 파일 개수가 업데이트되어 조회됨
```python
import os

class DirectorySize:

    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))

class Directory:

    size = DirectorySize()              # Descriptor instance

    def __init__(self, dirname):
        self.dirname = dirname          # Regular instance attribute
```
```python
>>> s = Directory('songs')
>>> g = Directory('games')
>>> s.size                              # The songs directory has twenty files
20
>>> g.size                              # The games directory has three files
3
>>> os.remove('games/chess')            # Delete a game
>>> g.size                              # File count is automatically updated
2
```
### Descriptor 사용 예시(2) : Attribute access 관리
- Python Descriptor official 자료가 좋지않아 예제를 약간 변형함.
- 다음 코드는 [여기](https://github.com/Junhojuno/TIL-v2/blob/main/descriptor/02_descriptor2.py)와 동일함.
```python
import logging


logging.basicConfig(format='%(asctime)s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')


class LoggedScoreAccess:
    def __init__(self, value=50):
        self.value = value
        
    def __get__(self, obj, objtype=None):
        logging.debug('Accessing %r giving %r', 'score', self.value)
        return self.value
    
    def __set__(self, obj, value):
        logging.debug('Updating %r giving %r', 'score', self.value)
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

```
```python
>>> 2021-05-01 20:53:25 Accessing 'score' giving 50
>>> 50
>>> 2021-05-01 20:53:25 Accessing 'score' giving 50
>>> 2021-05-01 20:53:25 Updating 'score' giving 50
>>> 2021-05-01 20:53:25 Accessing 'score' giving 70
>>> 70
>>> 
>>> 2021-05-01 20:53:25 Accessing 'score' giving 70
>>> 70
>>> 2021-05-01 20:53:25 Accessing 'score' giving 70
>>> 2021-05-01 20:53:25 Updating 'score' giving 70
>>> 2021-05-01 20:53:25 Accessing 'score' giving 270
>>> 270
>>> 2021-05-01 20:53:25 Accessing 'score' giving 270
>>> 270
>>> vars(s1) :  {'name': 'Juno'}
>>> vars(s2) :  {'name': 'Kate'}
>>> s1.__dict__ :  {'name': 'Juno'}
>>> s2.__dict__ :  {'name': 'Kate'}
```
