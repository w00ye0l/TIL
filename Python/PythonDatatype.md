## 파이썬 기본 자료형(Python Datatype)

### 자료형 분류

- **불린형(Boolean Type)**
  - `True` / `False` 값을 가진 타입은 `bool`
  - 비교/논리 연산을 수행함에 있어서 활용
  - 다음은 모두 `False`로 변환
    - `0, 0.0, (), [], {}, '', None`
- **수치형(Numeric Type)**
  - `int` (정수, integer)
  - `float` (부동소수점, 실수, floating point number)
  - `complex` (복소수, complex number)
- **문자열(String Type)**
- **None**
  - 자료형 중의 하나, 아무 값도 없는 것을 의미함



### 논리 연산자(Logical Operator)

> 논리식을 판단하여 참(True)와 거짓(False)를 반환함

|  A and B   |       A와 B 모두 True면 True        |
| :--------: | :---------------------------------: |
| **A or B** | **A 또는 B가 하나라도 True면 True** |
| **not A**  |         **A의 반대의 결과**         |



### 수치형(Numeric Type)

- **정수형(int)**

  > 모든 정수의 타입은 `int`

  - Python 3부터는 `long` 타입은 없고, **모든 타입은 `int`**

  - **오버플로우 걱정 없음!**

- **실수형(float)**

  > 정수가 아닌 모든 실수는 `float` 타입

  - `Floating point rounding error`

    - 부동소수점에서 실수 연산 과정에서 발생 가능

      - 값 비교하는 과정에서 정수가 아닌 실수인 경우 주의할 것
    - 매우 작은 수보다 작은지를 확인하거나 `math` 모듈 활용

    ```python
    # 1. 임의의 작은 수
    abs(a - b) <= 1e-10
    
    # 2. math 모듈 활용
    import math
    math.isclose(a, b)
    ```

- **복소수(Complex)**

  > 실수부와 허수부로 구성된 복소수는 모두 `complex` 타입

  - 허수부를 j로 표현

  ```python
  a = 3 + 4j
  type(a)
  # <class 'complex'>
  a.real
  # 3.0
  a.imag
  # 4.0
  ```




### 산술 연산자(Arithmetic Operator)

> 기본적인 사칙연산 및 수식 계산

|    +     |     덧셈     |
| :------: | :----------: |
|  **-**   |   **뺄셈**   |
|  **\***  |   **곱셈**   |
|  **%**   |  **나머지**  |
|  **/**   |  **나눗셈**  |
|  **//**  |    **몫**    |
| **\*\*** | **거듭제곱** |



### 복합 연산자(In-place Operator)

> 연산과 할당이 함께 이뤄짐

|     a += b     |    a = a + b     |
| :------------: | :--------------: |
|   **a -= b**   |  **a = a - b**   |
|  **a \*= b**   |  **a = a * b**   |
|   **a /= b**   |  **a = a / b**   |
|  **a //= b**   |  **a = a // b**  |
| **a \*\* = b** | **a = a \*\* b** |



### 비교 연산자(Comparison Operator)

> 값을 비교하며, `True` / `False` 값을 리턴함

|   <    |     미만      |
| :----: | :-----------: |
| **<=** |   **이하**    |
| **>**  |   **초과**    |
| **>=** |   **이상**    |
| **==** |   **같은**    |
| **!=** | **같지 않음** |





### 문자열(String Type)

> 모든 문자는 `str` 타입

- 문자열은 작은 따옴표(`''`)나 큰 따옴표(`""`)를 활용하여 표기

- 중첩따옴표(Nested Quotes)

  - 따옴표 안에 따옴표를 표현할 경우

    - 작은 따옴표가 들어 있는 경우는 큰 따옴표로 문자열 생성
    - 큰 따옴표가 들어 있는 경우는 작은 따옴표로 문자열 생성

    ```python
    print("문자열 안에 '작은 따옴표'를 사용하려면 큰 따옴표로 묶는다.")
    print('문자열 안에 "작은 따옴표"를 사용하려면 큰 따옴표로 묶는다.')
    ```

- 삼중따옴표(Triple Quotes)

  - 작은 따옴표나 큰 따옴표를 삼중으로 사용

    - 따옴표 안에 따옴표를 넣을 때
    - 여러 줄을 나눠 입력할 때 편리

    ```python
    print('''문자열 안에 '작은 따옴표'나
    "큰 따옴표"를 사용할 수 있고
    여러 줄을 사용할 때도 편리하다.''')
    ```




### 인덱싱(Indexing)

> 인덱스를 통해 특정 값에 접근할 수 있음

```python
str = 'Korea'

print(str[0]) # K
print(str[-1]) # a
```



### 문자열 슬라이싱(Slicing)

```python
str = 'abcde'
print(str[1:3]) # bc
```

- 파이썬은 음의 인덱스도 가지고 있다!


```python
s = 'abcde'
print(s[-3:-1]) # cd
```

- Step


```python
s = 'abcdefghi'
print(s[2:5:2]) # ce
```

```python
s = 'abcdefghi'
print(s[5:2:-1]) # fed
```

```python
s = 'abcdefghi'
print(s[:3]) # abc
print(s[5:]) # fghi
```

```python
s = 'abcdefghi'
print(s[::]) # abcdefghi
print(s[::-1]) # ihgfedcba
```



### 문자열 응용

- **결합(Concaternation)**

  ```python
  'hello, ' + 'python!'
  # hello, python!
  ```

- **반복(Repetition)**

  ```python
  'hi!' * 3 
  # hi!hi!hi!
  ```

- **포함(Membership)**

  ```python
  'a' in 'apple' 
  # True
  'app' in 'apple'
  # True
  ```



### 문자열 활용

- `Escape Sequence`

  - 문자열 내에서 특정 문자나 조작을 위해서 역슬래시(`\`)를 활용하여 구분

  | 기호 |       의미        |
  | :--: | :---------------: |
  |  \n  |      줄 바꿈      |
  |  \t  |        탭         |
  |  \r  |    캐리지리턴     |
  |  \0  |     널(Null)      |
  | \\\  |        \\         |
  | \\'  | 단일인용부호(`'`) |
  | \\"  | 이중인용부호(`"`) |

    

- 문자열 안에 변수 넣기

  ```python
  score = 100
  print('내 점수는 ' + score + '이야.')
  # 오류 발생
  
  print(f'내 점수는 {score}이야.')
  print(f'원주율은 {pi}고, 원 넓이는 {pi*r*2}')
  ```

  ```python
  # %-formatting
  name = 'Kim'
  score = 4.5
  
  print('Hello, %s' % name)
  print('내 성적은 %d' % score)
  print('내 성적은 %f' % score)
  ```



### 문자열 특징

- Immutable : 변경 불가능함

  ```python
  a = 'my string?'
  a[-1] = '!'
  # 오류 발생
  ```

- Iterable : 반복 가능함

  ```python
  a = '123'
  for char in a:
      print(char)
  ```



### 자료형 변환(Typecasting)

> 파이썬에서 데이터 형태는 서로 변환할 수 있음

- 암시적 형 변환(Implicit)

  > 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우

- 명시적 형 변환(Explicit)

  > 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우

  - `str*`, `float` => `int`
  - `str*`, `int` => `float`
  - `int`, `float`, `list`, `tuple`, `dict` => `str`