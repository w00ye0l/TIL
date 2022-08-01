# 모듈, 패키지, 라이브러리
## 모듈
> 다양한 기능을 하나의 파일로 묶어놓은 것
- 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것

## 패키지
> 다양한 파일을 하나의 폴더로 묶어놓은 것
- 특정 기능과 관련된 여러 모듈의 집합
- 패키지 안에는 또 다른 서브 패키지를 포함

## 라이브러리
> 다양한 패키지를 하나의 묶음으로 묶어놓은 것

## pip
> 모듈, 패키지, 라이브러리를 관리하는 관리자

### 파이썬 표준 라이브러리(Python Standard Library, PSL)
- 파이썬에 기본적으로 설치된 모듈과 내장 함수
  - [https://docs.python.org/ko/3/library/index.html](https://docs.python.org/ko/3/library/index.html)

# 모듈과 패키지 활용
```python
import module
from module import var, function, Class
from module import *

from package import module
from package.module import var, function, Class
```

# 모듈 사용 예시
```python
import datetime

now = datetime.datetime.now()
print(now, type(now))

############

from datetime import datetime

now = datetime.now()
print(now, type(now))

# 2022-07-15 18:06:34.387197 <class 'datetime.datetime'>
```

```python
import random

numbers = random.sample(range(1, 46), 6)
numbers.sort()
print(numbers, type(numbers))
# [8, 29, 30, 31, 39, 41] <class 'list'>
```

# 파일 관리
## 파일 읽고 쓰기
```python
# open('파일 명', '모드', 인코딩 설정)

f = open('test.txt', 'w', encoding='utf-8')
f.close()

###########

with open('test.txt', 'w', encoding='utf-8') as f:
# 같은 코드지만 with를 사용하지 않는다면 .close()를 해주어야 함
# with를 사용하면 블럭을 벗어났을 때 자동 close
```
```python
with open('test.txt', 'w', encoding='utf-8') as f:
  f.write('Hello\n')
  for i in range(1, 6):
    f.write(f'{i} 번째 줄~\n')
```
- `'r'` : read (읽기 전용)
- `'w'` : write (쓰기 전용 - 덮어쓰기)
- `'a'` : append (쓰기, 파일이 이미 존재하면 이어서 쓰기)

```python
with open('test.txt', 'w', encoding='utf-8') as f:
  text = f.read()
  print(text, type(text))
  names = text.split()
  cnt =0

  for name in names:
    if name.startswith('김'): # '김'으로 시작하는 이름
    # 끝나는 문자를 확인하는 함수 => endswith()
      cnt+=1
  
  print(cnt)
```

```python
with open('test.txt', 'w', encoding='utf-8') as f:
  lines = f.readline()
  print(lines, type(lines))
  # 한 줄을 읽음, 타입은 str
  # 계속 반복하면 한 줄씩 계속 읽음

  for line in f:
    print(line, end='')
  # 끝까지 읽기

  lines = f.readlines()
  print(lines, type(lines))
  # 타입은 리스트, '\n'까지 붙어서 리스트에 저장됨
```

# json 관리
> JSON 는 Douglas Crockford가 널리 퍼뜨린 Javascript 객체 문법을 따르는 문자 기반의 데이터 포맷
```python
import json

f = open('stocks.json', 'r', encoding='utf-8')
kospi = json.load(f)

samsung = kospi
# 딕셔너리로 저장됨
print(samsung, type(samsung))

samsung = kospi['stocks']
# 리스트로 저장됨
# samsung = kospi['stocks'][0]으로 인덱스 활용 가능
print(samsung, type(samsung))
```