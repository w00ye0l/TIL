# 딕셔너리(Dictionary)

## 1. 해시 테이블

> 파이썬에는 딕셔너리(dict) 자료구조가 내장 되어 있다
>
> Non-sequence & Key-Value (Key는 immutable: 변경 불가능)

- **해시 함수** : 임의 길이의 데이터를 고정 길이의 데이터로 매핑하는 함수
- **해시** : 해시 함수를 통해 얻어진 값

<br/>

### 파이썬의 딕셔너리(Dictionary의 특징)

- 해시 함수와 해시 테이블을 이용하기 때문에 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠르다
- Hash function을 이용한 산술 계산으로 값이 있는 위치를 바로 알 수 있기 때문

<br/>

### 딕셔너리 연산의 시간 복잡도 (vs 리스트)

| 연산 종류   | 딕셔너리(Dictionary) | 리스트(List)   |
| ----------- | -------------------- | -------------- |
| Get Item    | O(1)                 | O(1)           |
| Insert Item | O(1)                 | O(1) 또는 O(N) |
| Update Item | O(1)                 | O(1)           |
| Delete Item | O(1)                 | O(1) 또는 O(N) |
| Search Item | O(1)                 | O(N)           |

<br/>

### 딕셔너리는 언제 사용해야 할까?

1. 리스트를 사용하기 힘든 경우
2. 데이터에 대한 빠른 접근 탐색이 필요한 경우
3. 현실 세계의 대부분의 데이터를 다룰 경우

<br/>

## 2. 딕셔너리 기본 문법

### 기본적인 딕셔너리 사용법 (선언)

> 변수 = { 'key1':'value1', 'key2':'value2', 'key3':'value3' ... }

<br/>

### 기본적인 딕셔너리 사용법 (삽입/수정)

> 딕셔너리['key'] = 'value'
>
> 내부에 해당 key가 없으면 삽입, 있으면 수정

<br/>

### 기본적인 딕셔너리 사용법 (삭제)

> - 딕셔너리.pop(key)
>
> 내부에 존재하는 key에 대한 value 삭제 및 반환, 존재하지 않는 key에 대해서는 KeyError 발생
>
> - 딕셔너리.pop(key, default)
>
> 두 번째로 인자로 default(기본)깂을 지정하여 KeyError 방지 가능

<br/>

### 기본적인 딕셔너리 사용법 (조회)

> - 딕셔너리['key']
>
> key에 해당하는 value 반환, key 값이 없으면 KeyError
>
> - 딕셔너리.get('key')
>
> key에 해당하는 value 반환, key 값이 없으면 None 반환

<br/>

## 3. 딕셔너리 메서드

### 1) .keys()

> 딕셔너리의 key 목록이 담긴 dict_keys 객체 반환

```python
john = {
    'name': 'john',
    'role': 'ceo'
}

for elem in john:
    print(elem)
# name, role
```

### 2) .values()

> 딕셔너리의 value 목록이 담긴 dict_values 객체 반환

```python
john = {
    'name': 'john',
    'role': 'ceo'
}

for elem in john:
    print(john[elem])
# john, ceo
```

### 3) .items()

> 딕셔너리의 (key, value) 쌍 목록이 담긴 dict_items 객체 반환

```python
john = {
    'name': 'john',
    'role': 'ceo'
}

for k, v in john.items():
    print(k, v)
# name john
# role ceo
```

