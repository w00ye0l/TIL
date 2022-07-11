# Python 기초

> 파이썬은 **컴퓨터 프로그래밍 언어(Computer Programming Language)**

## 컴퓨터(Computer)

> Caculation + Remember
>
> 계산을 하고 기억하는 것

## 프로그래밍(Programming)

> 명령어의 모음(집합)

## 언어(Language)

> 자신의 생각을 나타내고 전달하기 위해 사용하는 체계
>
> 문법적으로 맞는 말의 집합



- **선언적 지식(declarative knowledge)**

	> "사실에 대한 내용"

- **명령적 지식(imperative knowledge)**

	> "How-to"



## 파이썬(Python)이란?

- **Easy to learn**
  - 다른 프로그래밍 언어보다 문법이 간단하면서도 엄격하지 않음
    - 변수에 별도의 타입 지정이 필요 없음
  - 문법 표현이 매우 간결하여 프로그래밍 경험이 없어도 짧은 시간 내에 마스터할 수 있음
    - 예시 : 문장을 구분할 대 중괄호 대신 들여쓰기 사용
- **Expressive Language**
  - 같은 작업에 대해서도 C나 자바로 작성할 때보다 더 간결하게 작성 가능
- **크로스 플랫폼 언어**
  - 윈도우즈(Windows), MacOS, 리눅스(Linux), 유닉스(Unix) 등 다양한 운영체제에서 실행가능
- **인터프리터 언어(Interpreter)**
  - 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
  - 코드를 대화하듯 한 줄 입력하고 실행한 후, 바로 확인할 수 있음
- **객체 지향 프로그래밍(Object Oriented Programming)**
  - 파이썬은 객체지향 언어이며, 모든 것이 객체로 구현되어 있음
    - 객체(object) : 숫자, 문자, 클래스 등 값을 가지고 있는 모든 것 / 어떠한 것



## 코드 스타일 가이드

- 코드를 '어떻게 작성할지'에 대한 가이드라인
- 파이썬에서 제안하는 스타일 가이드
  - PEP8 [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
- 기업, 오픈소스 등에서 사용되는 스타일 가이드
  - Google Style guide [https://google.github.io/styleguide/pyguide.html](https://google.github.io/styleguide/pyguide.html)



## 들여쓰기(Identation)

> Space Sensitive

- 문장을 구분할 때, 들여쓰기를 사용
- 들여쓰기를 할 때는 `4칸(space키 4번)` 혹은 `1탭(Tab키 1번)`을 입력
  - **주의! 한 코드 안에서는 반드시 한 종류의 들여쓰기 사용!**



## 변수(Variable)란?

> 컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- 동일 변수에 다른 객체를 언제든 할당할 수 있기 때문에 
- 변수는 할당 연산자(`=`)를 통해 값을 할당(assignment)
- `type()`
  - 변수에 할당된 값의 타입
- `id()`
  - 변수에 할당된 값(객체)의 고유한 아이덴티티(identity) 값이며, 메모리주소



## 식별자(Identifiers)

- 파이썬 객체(변수, 함수, 모듈, 클래스 등)를 식별하는데 사용하는 이름
- 규칙
  - 식별자의 이름은 영문 알파벳, 언더스코어(`_`), 숫자로 구성
  - 첫 글자에 숫자가 올 수 없음
  - 길이제한이 없고, 대소문자를 구별
  - 예약어는 사용할 수 없음
  - 내장함수나 모듈 등의 이름으로도 만들면 안됨
    - 기존의 이름에 다른 값을 할당하게 되므로 더 이상 동작하지 않음



## 주석(Comment)

- 한 줄 주석
  - 주석으로 처리될 내용 앞에 '`#`'을 입력
    - 한 줄을 온전히 사용할 수도 있고, 그 줄 코드 뒷 부분에 사용 가능

