# 파이썬



## 함수

> 특정한 기능을 하는 코드의 조각(묶음)
>
> 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요시만 호출하여 간편하게 사용

- 함수를 사용하는 이유

  - Decomposition : 기능을 분해, 재사용 가능
  - Abstraction : 복잡한 내용을 숨기고, 기능에 집중하여 사용할 수 있음, 재사용성, 가독성, 생산성 (블랙박스)

- 사용자 함수(Custom Function)

  - 구현되어 있는 함수가 없는 경우, 사용자가 직접 함수를 작성 가능

  ```python
  def function_name:
      # code block
      return returning_value
  ```

  



### 함수 기본 구조

- 선언과 호출
  - 함수의 선언은 `def` 키워드를 활용
  - 들여쓰기를 통해 `Function Body`(실행될 코드 블록)를 작성
  - 함수는 `parameter`를 넘겨줄 수 있음
  - 함수는 동작 후 `return`을 통해 결과값을 전달
  - 함수는 `함수명()`으로 호출
    - paramter가 있는 경우, `함수명(값1, 값2, ...)`로 호출



- 함수의 결과값(Output)

  - 함수는 반드시 값을 하나만 return

    - 명시적인 return이 없는 경우에도 None을 반환

  - 함수는 return과 동시에 실행이 종료

    ```python
    def minus_and_product(x, y):
        return x - y
    	return x * y	# 이 return은 실행되지 않고 함수 종료
    ```

  - `return 값1, 값2` : 이 방식으로 return할 경우 tuple 형태 `(값1, 값2)`로 묶여 반환

    ```python
    def minus_and_product(x, y):
        return x - y, x * y # tuple로 묶여 (x - y, x * y)로 출력됨
    ```

  - `print `함수는 출력을 해주고, return 값은 없음 (None)

    ```python
    def no():
        a = 1
        
    result = no()
    print(result, type(result)) # None <class 'NoneType'>
    ```



- 함수의 입력(Input)

  >  Parameter : 함수를 실행할 때, 함수 내부에서 사용되는 식별자
  >
  > Argument : 함수를 호출할 때, 넣어주는 값

  ```python
  def function(ham): # parameter : ham
      return ham
  
  function('spam')   # argument : 'spam'
  ```

  - Argument

    > 함수 호출 시 함수의 parameter를 통해 전달되는 값
    >
    > Argument는 소괄호 안에 할당 `func_name(argument)`
    >
    > - 필수 Argument : 반드시 전달되어야 하는 argument
    > - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본 값이 전달

    - positional arguments

      - 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨

      ```python
      def add(x, y):
          return x + y
      
      add(2, 5)
      ```

    - keyword arguments

      - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
      - Keyword Argument 다음에 Positional Argument를 활용할 수 없음

      ```python
      def add(x, y):
          return x + y
      
      add(x=2, y=5)
      add(2, y=5)
      add(x=2, 5) # 안됨
      ```

    - Default Arguments Values

      - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
        - 정의된 것보다 더 적은 개수의 argument들로 호출 될 수 있음

      ```python
      def add(x, y=0):
          return x + y
      
      add(2) 		# 2
      add(2, 5) 	# 7
      ```

    - 정해지지 않은 개수의 arguments

      - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
      - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

      ```python
      def add(*args):
          for arg in args:
              print(arg)
              
      add(2)
      add(2, 3, 4, 5)
      ```

    - 정해지지 않은 개수의 keyword arguments

      - 함수가 임의의 개수 Argument를 Keyword Argument로 호줄될 수 있도록 지정
      - Argument들은 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현

      ```python
      def family(**kwargs):
          for key, value in kwargs:
              print(key, ":", value)
              
      family(father='John', mother='Jane', me='John Jr.')
      ```

      

### 함수의 범위(Scope)

> 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분

- scope
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  - local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능
- variable
  - global variable : global scope에 정의된 변수
  - local variable : local scope에 정의된 변수



- 객체 수명주기
  - 객체는 각자의 수명주기(lifecycle)가 존재
    - bulit-in scope
      - 파이썬이 실행된 이후부터 영원히 유지
    - global scope
      - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    - local scope
      - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
- 이름 검색 규칙(Name Resolution)
  - 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
  - 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
    - Local scope : 함수
    - Enclosed scope : 특정 함수의 상위 함수
    - Global scope : 함수 밖의 변수, Import 모듈
    - Bulit-in scope : 파이썬 안에 내장되어 있는 함수 또는 속성
  - 함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음



### 함수 응용

- `map(function, iterable)`

  > 순회 가능한 데이터 구조(iterable)의 모든 요소에 함수(function)를 적용하고, 그 결과를 map object로 반환

  - `n, m = map(int, input().split())`
    - `input()` : 타입은 항상 string
    - `문자열.split()` : 구분값을 기준으로 쪼개고 반환 결과는 항상 리스트
    - `map` : 어떤 함수를 반복 가능한 것들의 요소에 모두 적용시킨 결과
      - `int` 함수를 `input().split()` 리스트의 모든 요소에 적용한 결과 => `map object`(맵 어떤 것)