# 입력 & 출력

## 1. 입력 활용 예시 (input)

> input()은 사용자의 입력 한 줄을 문자열로 받는 함수

```python
word = input()
>>> happyhacking
```

- `input()`과 `map()`을 이용해 원하는 대로 입력 받기

  ```python
  # 문자열 입력 받기
  a = input()
  
  # 한 개 숫자 입력 받기
  b = int(input())
  c = float(input())
  
  # 여러 개 숫자 입력 받기
  d, e = map(int, input().split())
  f, g, h = map(float, input().split())
  ```

- 파이썬의 내장 함수 `map(funcition, iterable)`

  ```python
  map(int, ["1", "2", "3"])
  # 각 요소를 정수로 반환
  ```



## 2. 출력 활용 예시 (print)

> print()는 데이터를 출력할 수 있는 함수이며, 자동적으로 줄 바꿈 발생

- `print()`

  - 콤마`(,)`를 이용해 여러 인자를 넣으면 공백을 기준으로 출력
  - end, sep 옵션을 사용하여 출력 조작하기

  ```python
  a, b, c = map(int, input().split())
  >>> 1 2 3
  
  print(a, b, c, end = '&')
  >>> 1 2 3&
  ```

