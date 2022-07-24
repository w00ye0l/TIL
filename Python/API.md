# API

> Application Programming Interface

- 컴퓨터나 컴퓨터 프로그램 사이의 연결
- 일종의 소프트웨어 인터페이스이며 다른 종류의 소프트웨어에 서비스를 제공
- 사용하는 방법을 기술하는 문서나 표준은 API 사양/명세 (specification)



## API를 사용하기 전에 확인해야 할 것?

- 어떻게 조작하는지
- 요청(정보를 원하는 사람) **-> 주소(Url) ->** 응답(정보를 주는 사람)
- 요청(정보를 원하는 사람) **<- 문서(JSON) <-** 응답(정보를 주는 사람)



## API 활용시 확인 사항

- 요청하는 방식에 대한 이해
  - 인증 방식
  - URL 생성
    - 기본 주소
    - 원하는 기능에 대한 추가 경로
    - 요청 변수 (필수와 선택)
- 응답 결과에 대한 이해
  - 응답 결과 타입 (JSON)
  - 응답 결과 구조



## API 활용 예시

### 1. 비트코인 시세 확인하기

```python
import pprint
# pip install requests
import requests
# URL로 요청을 보내서
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# 요청을 보내서
response = requests.get(URL)
# 응답 받은 값을 가져온다.
# <Response [200]> <class 'requests.models.Response'>
print(response, type(response))

# 속성 예시
print(response.status_code)  # 200
print(response.text, type(response.text))  # 문자열

# 메서드 예시
# .json() 텍스트 형식의 JSON 파일을 파이썬 데이터 타입으로 변경!
print(response.json(), type(response.json()))  # <class 'dict'>

print('=====================================')

data = response.json()
pprint.pprint(data.get('data').get('closing_price')) # '29865000'
```



### 2. agify.io에서 나이 확인하기

```python
# https://api.agify.io?name=michael

import requests

URL = 'https://api.agify.io'
params = {
    'name': 'key'
}
response = requests.get(URL, params=params).json()
print(response)
```



### 2.1 agify.io를 random 함수로 구현해보기

```python
import random

print('======나이를 알려드립니다======')
name = input('이름을 입력해주세요: ')
print('===============================')
# 지영
# ord('지') # 문자 => 숫자
# ord('영') # 문자 => 숫자
# 합한 겂을 가져가면 이름마다 같게 나온다.
random.seed(10)
# choice(a) 는 하나 고르기
# sample(a, b) 는 a에서 b개 고르기
print(f'{random.choice(range(10, 90))}살 입니다.')
```



### 3. Lotto 활용

```python
import requests

for n in range(1, 10):
    URL = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'
    response = requests.get(URL).json()

    print(response)
```



## TMDB API 활용 예시

### 1. TMDB 활용

```python
# API key
# API link
import requests

BASE_URL = <API LINK>
path = 'movie/76341'
params = {
    'api_key': <API key>,
    'language': 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)
```

