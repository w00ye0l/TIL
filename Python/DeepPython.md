# 파이썬 응용/심화

## 추가 문법

- List Comprehension

  - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
  - `[<expression> for <변수> in <iterable>]`
  - `[<expression> for <변수> in <iterable> if <조건식>]`

  ```python
  # 1~3의 세제곱의 결과가 담긴 리스트를 만드시오.
  cubic_list = []
  for number in range(1, 4):
      cubic_list.append(number**3)
  print(cubic_list)
  
  # List Comprehension
  [number**3 for number in range(1, 4)]
  
  # 짝수 리스트
  even_list = [i for i in range(10) if i % 2 == 0]
  # [0, 2, 4, 6, 8]
  ```

- Dictionary Comprehension

  - `{key: value for <변수> in <iterable>}`
  - `{key: value for <변수> in <iterable> if <조건식>}`

  ```python
  # 1~3의 세제곱의 결과가 담긴 딕셔너리를 만드시오.
  cubic_dict = {}
  for number in range(1, 4):
      cubic_dict[number] = number ** 3
  print(cubic_dict)
  
  # Dictionary Comprehension
  {number: number**3 for number in range(1, 4)}
  ```

- lambda [parameter] : 표현 식

  - 람다 함수
    - 표현 식을 계산한 결괏값을 반환하는 함수로, 이름이 없는 함수여서 익명 함수 라고도 불림
  - 특징
    - return문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
  - 장점
    - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
    - def를 사용할 수 없는 곳에서도 사용 가능

  ```python
  def is_3(n):
      return n % 3 == 0
  
  
  def is_3_1(n):
      if n % 3 == 0:
          return n
  
  
  numbers = [1, 2, 5, 10, 3, 9, 12]
  
  m_result = list(map(is_3, numbers))
  m_result_1 = list(map(is_3_1, numbers))
  m_result_2 = list(map(lambda n: n % 3 == 0, numbers))
  
  f_result = list(filter(is_3, numbers))
  f_result_1 = list(filter(is_3_1, numbers))
  f_result_2 = list(filter(lambda n: n % 3 == 0, numbers))
  
  print(m_result)  # [False, False, False, False, True, True, True]
  print(m_result_1)  # [None, None, None, None, 3, 9, 12]
  print(m_result_2)  # [False, False, False, False, True, True, True]
  
  print(f_result)  # [3, 9, 12]
  print(f_result_1)  # [3, 9, 12]
  print(f_result_2)  # [3, 9, 12]
  
  # map : 요소별로 함수를 적용하여 반환하는 함수
  # filter : True인 요소를 반환하는 함수
  ```

  



# 모듈 심화

## 모듈

> 다양한 기능을 하나의 파일로 -> 모듈
>
> 다양한 파일을 하나의 폴더로 -> 패키지
>
> 다양한 패키지를 하나의 묶음으로 -> 라이브러리
>
> 이 것을 관리하는 관리자(pip)

- 파이썬 표준 라이브러리(Python Standard Library, PSL)
  - 파이썬에 기본적으로 설치된 모듈과 내장 함수
- 파이썬 패키지 관리자(pip)
  - PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템



## 패키지 활용 명령어

- 패키지 설치
  - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치 할 수 있음
  - `$ pip install requests`
- 패키지 삭제
  - pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌
  - `$ pip uninstall SomePackage`
- 패키지 목록 및 특정 패키지 정보
  - `$ pip list` : 패키지 목록
  - `$ pip show SomePackage` : 특정 패키지 정보 ex) `$ pip show requests`
- 패키지 freeze
  - 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력
  - 해당하는 목록을 requirements.txt(관습)으로 만들어 관리함
  - `$ pip freeze`



## 가상 환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야 함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
  - 과거 외주 프로젝트 - django 버전 2.x
  - 신규 회사 프로젝트 - django 버전 3.x
- 이러한 경우 가상 환경을 만들어 프로젝트 별로 독립적인 패키지를 관리할 수 있음



### 파이썬 실행에 대한 이해

- python은 특정 경로에 있는 프로그램을 실행시키는 것

  - `$ which python`

  ```python
  # 가상 환경 생성
  $ python -m venv venv
  # 가상 환경 실행
  $ source venv/Scripts/activate
  # 가상 환경 패키지 목록 확인
  $ pip list
  # 가상 환경 패키지 공유
  $ pip freeze > requirements.txt
  ```

  

# URL을 이용한 요청 맛보기

```python
import requests
URL = 'https://api.bithumb.com/public/ticker/ALL_KRW'
response = requests.get(URL).json()
print(response)
```

