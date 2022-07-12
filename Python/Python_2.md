# 파이썬

## 기본 문법

- 입력

  ```python
  # 기본 입력
  a = input()
  
  # 형 변환 입력
  a = int(input())
  
  # 동시에 두 개의 값 입력(공백으로 구분)
  a, b = input().split()
  
  # 동시에 두 개의 값 입력(콜론으로 구분)
  a, b = input().split(':')
  
  # 한 줄에 하나씩 두 개의 값 입력
  a = input()
  b = input()
  ```

  - 기본 입력은 `str`인 문자열로 선언되기 때문에 숫자 계산을 위해서는 `int`로 형 변환을 해주어야 함



## 제어문

>- 파이썬은 기본적으로 위에서 아래로 순차적으로 명령을 수행
>
>- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요
>
>- 제어문은 순서도(flow chart)로 표현이 가능



### 0. 조건문

> 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

- 기본 형식

  - expression에는 참/거짓에 대한 조건식
    - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블럭을 실행
    - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행

  ```python
  if < expression >:
      # Run this Code block
  else:
      # Run this Code block
  ```

  - 조건문에서는 `else` 생략 가능



### 1. 복수 조건문

> 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

```python
if <expression>:
    # Code block
elif <expression>:
    # Code block
elif <expression>:
    # Code block
else:
    # Code block
```

- 예제

  ```python
  dust = int(input())
  if dust > 150:
      print('매우 나쁨')
  elif dust > 80:
      print('나쁨')
  elif dust > 30:
      print('보통')
  else:
      print('좋음')
  ```



### 2. 중첩 조건문

> 조건문 안에 조건문을 입력

```python
if <expression>:
    if <expression>:
        # Code block
    # Code block
else:
    # Code block
```



### 3. 조건 표현식

> - 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용
>
> - 삼항 연산자(Ternary Operator)라고 불리기도 함

```python
# <true인 경우 값> if <expression> else <false인 경우 값>
value = num if num >= 0 else -num
```



## 반복문

> 특정 조건을 도달할 때까지, 반복되는 일련의 문자

- while 문
  - 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
- for 문
  - 반복가능한 객체를 모두 순회하면 종료 ( 별도의 종료조건이 필요 없음)
- 반복 제어
  - break, continue, for-else



### 0. while 문

> 조건식이 참인 경우 반복적으로 코드를 실행

- 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨
- 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
- while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요

```python
while <expression>:
    # Code block
```



### 1. for 문

> 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable) 요소를 모두 순회함
>
> ​	처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음

```python
for <변수명> in <iterable>:
    # Code block
```

- 예시

  ```python
  for fruit in ['banana', 'mango', 'apple']:
  	print(fruit)
  print('end')	# banana mango apple
  
  #####
  
  chars = input()
  for char in chars:
      print(char)
  
  #####
  
  chars = input()
  for idx in range(len(chars)):
      print(chars[idx])
  ```



## 파이썬 심화

### 0. Enumerate 순회

> 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
>
> ​	(index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
members = ['민수', '영희', '철수']

for i in range(len(members)):
    print(f'{i} {members[i]}')

######

for i, member in enumerate(members): # [(0, '민수'), (1, '영희'), (2, '철수')]
    print(i, member) # 0 민수
```



### 1. Dictionary 순회

> 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

```python
grades = {'john': 80, 'eric': 90}
for name in grades:
    print(name) # john eric

#####

grades = {'john': 80, 'eric': 90}
for name in grades:
    print(name, grades[name]) # john 80 eric 90
```



## 반복문 제어

- break

  - 반복문 종료

  ```python
  for i in range(10):
      if i > 1:
          print('need 0 and 1!')
          break
      print(i)
  # 0 1 'need 0 and 1!'
  ```

- continue

  - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행

  ```python
  for i in range(6):
      if i % 2 == 0:
          continue
      print(i)
  # 1 3 5
  ```

- for-else

  - 끝까지 반복문을 실행한 후에 else문 실행
    - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음

  ```python
  for char in 'apple':
      if char == 'b':
          print('b!')
          break
  else:
      print('b가 없습니다.')
  # 'b가 없습니다.'
  
  ########
  
  for char in 'banana':
      if char == 'b':
          print('b!')
          break
  else:
      print('b가 없습니다.')
  # 'b!'
  ```

  
