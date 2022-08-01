# 데이터 구조(Data Structure)

## 메서드(Methods)

> 타입.메서드() => 주어.동사()

### 시퀀스

#### 문자열(String)

> 문자들의 나열(sequence of characters)
>
> 문자열은 작은 따옴표(`'`)나 큰 따옴표(`"`)를 활용하여 표기

- 문자열 탐색

  - .find(x)

    - x의 첫 번째 위치 인덱스를 반환, 없으면 '-1' 반환

    ```python
    'apple'.find('p')
    # 1
    'apple'.find('k')
    # -1
    ```

  - .index(x)

    - x의 첫 번째 위치 인덱스를 반환, 없으면 오류 발생

    ```python
    'apple'.find('p')
    # 1
    'apple'.find('k')
    # 에러 발생
    ```


- 문자열 검증

  - .isalpha(), .isupper(), .islower(), .istitle(), .isdecimal(), .isdigit(), .isnumeric()

- 문자열 변경

  - .replace(old, new[,count])

    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
    - count를 지정하면, 해당 개수만큼 시행

    ```python
    'coone'.replace('o', 'a')
    # caane
    'woooooowoo'.replace('o', '!', 2)
    # w!!oooowoo
    ```

  - .strip([chars])

    - 특정한 문자들을 지정하면, 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)
    - 문자열을 지정하지 않으면 공백을 제거함(`\n`가 포함 됨)

    ```python
    '    wow!\n'.strip()
    # 'wow!'
    '    wow!\n'.lstrip()
    # 'wow!\n'
    '    wow!\n'.rstrip()
    # '    wow!'
    'hello????'.rstrip()
    # 'hello'
    ```

  - .split(sep=None, maxsplit=-1)

    - 문자열을 특정한 단위로 나눠 리스트로 반환
      - sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음
      - maxsplit이 -1인 경우에는 제한이 없음

    ```python
    'a,b,c'.split('_')
    # ['a,b,c']
    'a b c'.split()
    # ['a', 'b', 'c']
    ```

  - 'separator'.join([iterable])

    - 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환

    ```python
    ''.join(['3', '5'])
    # 35
    ```

    - iterable에 문자열이 아닌 값이 있으면 TypeError 발생

      ```python
      names = ' '.join(map(str, [10, 20, 30]))
      # 리스트 안에 문자열이 아니기 때문에 map을 통해 형 변환 후 join
      print(names)
      ```

- 기타 변경

  - .capitalize(), .title(), .upper(), .lower(), .swapcase()


#### 리스트(List)

> 변경 가능한 값들의 나열된 자료형

- 추가 및 삭제

  - .append(x)
    - 리스트에 값을 추가함
  
    ```python
    abc = ['a', 'b', 'c']
    abc.append('d')
    print(abc)
    # ['a', 'b', 'c', 'd']
    ```
  
  - .extend(iterable)
      - 리스트에 반복 가능한 값들(iterable)을 분해하여 추가함
  
      ```python
      abc = ['a', 'b', 'c']
      abc.extend('fdnsklf')
      print(abc)
      # ['a', 'b', 'c', 'f', 'd', 'n', 's', 'k', 'l', 'f']
      ```
  
  - .insert(i, x)
      - 정해진 위치 i에 값을 추가함, i 값이 리스트 길이보다 큰 경우 맨 뒤에 추가됨
  
      ```python
      abc = ['a', 'b']
      abc.insert(0, 'abd')
      # ['abd', 'a', 'b']
      
      abc = ['a', 'b']
      abc.insert(10000, 'abd')
      # ['a', 'b', 'abd']
      ```
  
  - .remove(x)
      - 리스트에서 값이 x인 것 삭제, 없는 경우 Value Error
  
      ```python
      numbers = [1, 2, 3, 'hi']
      numbers.remove('hi')
      # [1, 2, 3]
      numbers.remove(4)
      # 에러 발생
      ```
  
  - .pop(i)
      - 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
      - i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함
  
      ```python
      numbers = [1, 2, 3, 'hi']
      pop_numbers = numbers.pop()
      # 'hi'
      
      numbers = ['hi', 1, 2, 3]
      pop_numbers = numbers.pop(0)
      # 'hi'
      ```
  
  - .clear()
      - 모든 항목을 삭제
  
      ```python
      numbers = [1, 2, 3]
      numbers.clear()
      # []
      ```
  
- 탐색 및 정렬

  - .index(x)
    - x값을 찾아 해당 index 값을 반환, 없는 x값을 입력할 경우 에러 발생
  
    ```python
    numbers = [1, 2, 3, 4]
    print(numbers.index(3))
    # 2
    print(numbers.index(100))
    # 에러 발생
    ```
  
  - .count(x)
      - 원하는 값의 개수를 반환
  
      ```python
      numbers = [1, 2, 3, 1, 1]
      numbers.count(1)
      # 3
      numbers.count(100)
      # 0
      ```
  
  - .sort()
      - 원본 리스트를 정렬함. None 반환
      - sorted 함수와 비교할 것
  
      ```python
      # 리스트 메서드 활용
      a = [10, 1, 100]
      new_a = a.sort()
      print(a, new_a)
      # [1, 10, 100] None
      # 리스트 메서드를 활용하면, 그 메서드를 정렬된 상태로 변경(원본 변경)
      # return 되는 것은 None
      
      # 리스트에 sorted 함수를 활용
      b = [10, 1, 100]
      new_b = sorted(b)
      print(b, new_b)
      # [10, 1, 100] [1, 10, 100]
      # sorted 함수를 활용하면, 원본을 변경하지 않음
      # return 되는 것은 정렬된 리스트
      ```
  
  - .reverse()
      - 순서를 반대로 뒤집음(정렬하는 것이 아님). None 반환
  
      ```python
      numbers = [3, 2, 5, 1]
      result = numbers.reverse()
      print(numbers, result)
      # [1, 5, 2, 3] None
      ```
  



### 컬렉션

#### 세트(Set)

> 유일한 값들의 모음

- 메서드를 잘 사용하지 않음

#### 딕셔너리(Dictionary)

> 키-값(key-value) 쌍으로 이루어진 모음

- 조회

  - .get(key[, default])

    - key를 통해 value를 가져옴
    - .get을 사용하지 않고 그냥 접근할 경우 key가 없으면 에러가 발생함
    - keyError가 발생하지 않으며, default 값을 설정할 수 있음(기본 : None)

    ```python
    my_dict = {'a': 1, 'b': 2}
    my_dict['c']
    # 에러 발생
    
    my_dict = {'a': 1, 'b': 2}
    print(my_dict.get('c'))
    # None
    print(my_dict.get('a'))
    # 1
    print(my_dict.get('c', 0))
    # 0
    ```

- 추가 및 삭제

  - .pop(key[, default])

    - key가 딕셔너리에 있으면 제거하고 해당 값을 반환
    - 그렇지 않으면 default를 반환
    - default 값이 없으면 KeyError

    ```python
    my_dict = {'a': 1, 'b': 2}
    data = my_dict.pop('a')
    print(data, my_dict)
    # 1 {'b': 2}
    
    my_dict = {'a': 1, 'b': 2}
    data = my_dict.pop('c')
    print(data, my_dict)
    # 에러 발생
    ```
  
  - .update([other])
  
    - 값을 제공하는 key, value로 덮어씀
  
    ```python
    my_dict = {'a': 1, 'b': 2}
    my_dict.update(a= 3)
    print(my_dict)
    # {'a': 3, 'b': 2}
    ```
  
    
