# 디버깅
> 개발 단계에서 발생하는 오류를 찾아내 원인을 밝히고 수정해 해결하는 것
-	제어가 되는 시점에서 확인한다. (조건/반복, 함수)
    - branches : 모든 조건이 원하는 대로 동작하는지
    - for loops : 반복문에 진입하는지, 원하는 횟수만큼 실행되는지
    - while loops : for loops와 동일, 종료조건이 제대로 동작하는지
    - function : 함수 호출시, 함수 파라미터, 함수 결과

# 에러/예외 처리(Error/Exception Handling)
## 문법 에러(Syntax Error)
-	syntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
-	파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
-	줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret) 기호(^)를 표시
-	EOL (End of Line)
    ```python
    print(‘hello
    ```
-	EOF (End of File)
    ```python
    print(
    ```
-	Invalid syntax
    ```python
    while
    ```
-	Assign to literal
    ```python
    5 = 3
    ```

## 예외(Exception)
-	실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
    - 문장이나 표현식이 문법적으로 올바르더라도 발생하는 에러
-	실행 중에 감지되는 에러들을 예외라고 부름
-	예외는 여러 타입(type)으로 나타나고, 타입이 메시지의 일부로 출력됨
    - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
-	모든 내장 예외는 Exception Class를 상속받아 이뤄짐
-	사용자 정의 예외를 만들어 관리할 수 있음
-	ZeroDivisionError : 0으로 나누었을 때
    - `10/0`
-	NameError : namespace 상에 이름이 없는 경우(선언되지 않은 변수 사용)
    - `print(name_error)`
-	TypeError : 타입불일치
    - `1 + ‘1’`, `round(‘3.5’)`
-	TypeError : arguments 부족
    ```python
    divmod()
    ########
    import random
    random.sample()
    ```
-	TypeError : argument 개수 초과
    ```python
    divmod(1, 2, 3)
    ########
    import random
    random.sample(range(3), 1, 2)
    ```	
-	ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우
    ```python
    int(‘3.5’)
    ########
    range(3).index(6)
    ```
-	IndexError : 인덱스 범위를 넘어가는 경우
    ```python
    empty_list = []
    empty_list[2]
    ```
-	KeyError : 키가 존재하지 않는 경우
    ```python
    song = {‘IU’: ‘좋은날’}
    song[‘BTS’]
    ```
-	ModuleNotFoundError : 존재하지 않는 모듈을 import 하는 경우
    ```python
    import nonamed
    ```
-	ImportError : Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
    ```python
    from random import samp
    ```
-	IndentationError : Indentation이 적절하지 않는 경우
    ```python
    for I in range(3):
    Print(i)
    ```
-	KeyboardInterrupt : 임의로 프로그램을 종료하였을 때
    ```python
    while True:
      continue
    ```

## 예외 처리
-	try 문(statement) / except 절(clause)을 이용하여 예외 처리를 할 수 있음
-	try문
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생되지 않으면, except 없이 실행 종료
-	except 문
    - 예외가 발생하면, except 절이 실행
    - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
    ```python
    number = input()

    try:
        print(100/int(number))
    except ZeroDivisionError as Error:
        print(Error)
        print('0으로 나눌 수 없습니다')
    except ValueError:
        print('숫자 형식을 입력해주세요')
    except Exception:
        print('오류')
    ```

## 예외 처리 정리
-	try
    -	코드를 실행함
-	except
    -	try 문에서 예외가 발생시 실행함
-	else
    -	try 문에서 예외가 발생하지 않으면 실행함
-	finally
    -	예외 발생 여부와 관계없이 항상 실행함
## 예외 발생시키기
-	raise statement
    - raise를 통해 예외를 강제로 발생
    - `raise <표현식>(메시지)`
