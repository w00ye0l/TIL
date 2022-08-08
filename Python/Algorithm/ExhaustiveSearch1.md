# 완전 탐색 1 (Exhaustive Search)

## 1. 무식하게 풀기 (Brute-force)

> Brute-force는 모든 경우의 수를 탐색하여 문제를 해결하는 방식

- 브루트포스(Brute-force)라고도 하며, 무식하게 밀어붙인다는 뜻
- 가장 단순한 풀이 기법이며, 단순 조건문과 반복문을 이용해서 풀 수 있음
- 복잡한 알고리즘보다는 아이디어를 어떻게 코드로 구현할 것인지가 중요

```python
# Brute Force
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
# 5개 중에서 3개를 고르는 조합
```

<br/>

## 2. 델타 탐색 (Delta Search)

> (0, 0)에서부터 이차원 리스트의 모든 원소를 순회하며(완전 탐색) 각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동하는 방식

- 이차원 리스트의 인덱스(좌표)의 조작을 통해서 상하좌우 탐색
- 이때 행과 열의 변량인 -1, +1을 델타(delta) 값이라고 한다

```python
# 델타(delta) 값을 이용해 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
    for y in range(m):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                x = nx
                y = ny
    
##################

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for x in range(n):
    for y in range(m):
        for d in delta:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < 3 and 0 <= ny < 3:
                x = nx
                y = ny
```

