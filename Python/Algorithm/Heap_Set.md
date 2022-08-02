# 힙 (Heap)

## 우선순위 큐(Priority Queue)

> 우선순위 큐(Priority Queue)는 우선순위(중요도, 크기 등 순서 이외의 기준)를 기준으로 가장 우선순위가 높은 데이터가 가장 먼저 나가는 방식
>
> 순서가 아닌 우선순위를 기준으로 가져올 요소를 결정(dequeue)하는 큐

1. 가중치가 있는 데이터
2. 작업 스케줄링
3. 네트워크

<br/>

### 우선순위 큐(Priority Queue)를 구현하는 방법

1. 배열(Array)
2. 연결 리스트(Linked List)
3. 힙(Heap)

<br/>

### 우선순위 큐 구현 별 시간 복잡도

| 연산 종류                | Enqueue(추가) | Dequeue(삭제) |
| ------------------------ | ------------- | ------------- |
| 배열(Array)              | O(1)          | O(N)          |
| 정렬된 배열              | O(N)          | O(1)          |
| 연결 리스트(Linked List) | O(1)          | O(N)          |
| 정렬된 연결 리스트       | O(N)          | O(1)          |
| **힙(Heap)**             | **O(logN)**   | **O(logN)**   |

<br/>

## 힙(Heap)의 특징

- 최댓값 또는 최솟값을 빠르게 찾아내도록 만들어 진 데이터 구조
- 완전 이진 트리의 형태로 느슨한 정렬 상태를 지속적으로 유지한다
- 힙 트리에서는 중복 값을 허용

<br/>

### Heap은 언제 사용해야 할까?

1. 데이터가 지속적으로 정렬되어야 하는 경우
2. 데이터에 삽입/삭제가 빈번할 때

<br/>

### 파이썬의 heapq 모듈

> Minheap(최소 힙)으로 구현되어 있음(가장 작은 값이 먼저 옴)
>
> ​	Miaxheap(최대 힙)으로 구현되어 있음(가장 큰 값이 먼저 옴)
>
> 삽입, 삭제, 수정, 조회 연산 속도가 리스트보다 빠르다
>
> (배열, 연결 리스트, 힙으로 구현 가능)

<br/>

| 연산 종류   | 힙      | 리스트       |
| ----------- | ------- | ------------ |
| Get Item    | O(1)    | O(1)         |
| Insert Item | O(logN) | O(1) or O(N) |
| Delete Item | O(logN) | O(1) or O(N) |
| Search Item | O(N)    | O(N)         |

<br/>

### 큐와 힙의 사용법 비교

- 큐
  - `enqueue`, `dequeue`
- 힙(Min)
  - `heapq.heappush()`, `heapq.heappop()`

<br/>

### 힙 딕셔너리 메서드

1. `heapq.heapify()`
2. `heapq.heappop(heap)`
3. `heapq.heappush(heap, item)`

```python
# 숫자를 입력받으면서 0일 때는 heap에서 숫자를 꺼내고 0이 아니면 heap에 숫자를 저장한다.
import heapq

heap = []

for _ in range(int(input())):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
```

```python
# 최대 힙 == 최소 힙의 역순
import heapq

heap = []

for i in range(int(input())):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (-num, num) 
        # heappush에 튜플 값을 넣어 (우선순위, 값)으로 push 가능하다.
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
			# heappush를 튜플로 했기 때문에 튜플의 인덱스 1 값인 원본 num을 출력
```

```python
# 절댓값 힙
import heapq

heap = []

for i in range(int(input())):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num), num) 
        # heappush에 튜플 값을 넣어 (우선순위, 값)으로 push 가능하다.
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
			# heappush를 튜플로 했기 때문에 튜플의 인덱스 1 값인 원본 num을 출력
```



<br/>

# 셋 (Set)

> 셋(set)은 수학에서 '집합'을 나타내는 데이터 구조로 Python에서는 기본적으로 제공되는 자료구조

<br/>

## Set의 연산

1. `.add()`
2. `.remove()`
3. `+ (합)`
4. `- (차)`
5. `& (교)`
6. `^ (대칭차)` == `+ (합집합) - & (교집합)`

<br/>

## Set은 언제 사용해야 할까?

1. 데이터의 중복이 없어야 할 때 (고유값들로 이루어진 데이터가 필요할 때)
2. 정수가 아닌 데이터의 삽입/삭제/탐색이 빈번히 필요할 때

<br/>

### 셋(Set) 연산의 시간 복잡도

| 연산 종류   | 시간 복잡도 |
| ----------- | ----------- |
| 탐색        | O(1)        |
| 제거        | O(1)        |
| 합집합      | O(N)        |
| 교집합      | O(N)        |
| 차집합      | O(N)        |
| 대칭 차집합 | O(N)        |

