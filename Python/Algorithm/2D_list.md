# 이차원 리스트

> 이차원 리스트는 리스트를 원소로 가지는 **리스트**일 뿐이다.
>
> `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
>
> 이차원 리스트는 **행렬(matrix)**이다.

<br/>

## 1. 특정 값으로 초기화 된 이차원 리스트 만들기

1. 직접 작성 (4 X 3 행렬)

   ```python
   matrix1 = [
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]
   ]
   ```

2. 반복문으로 작성 (100 X 100 행렬, n X m 행렬)

   ```python
   matrix = []
   
   for _ in range(100):
       matrix.append([0] * 100)
       
   ##############
   
   n, m = map(int, input().split())
   matrix = []
   
   for _ in range(n):
       matrix.append([0] * m)
   ```

3. 리스트 컴프리헨션으로 작성 (n X m 행렬)

   ```python
   n, m = map(int, input().split())
   
   matrix = [[0] * m for _ in range(n)]
   
   matrix[0][0] = 1
   
   print(matrix)
   # ex) n = 4, m = 3
   # [[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
   ```

4. 리스트 곱셈 연산

   ```python
   n, m = map(int, input().split())
   
   matrix = [[0] * m] * n
   
   matrix[0][0] = 1
   
   print(matrix)
   # ex) n = 4, m = 3
   # [[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
   ```

### 	[주의] 리스트 컴프리헨션 vs 리스트 곱셈 연산은 다르다!

<br/>

## 2. 입력 받기

1. 행렬의 크기가 **미리 주어지는 경우**

   ```python
   # 3 X 3 행렬
   matrix = [list(map(int, input().split())) for _ in range(3)]
   ```

2. 행렬의 크기가 **입력으로 주어지는 경우**

   ```python
   # n X m 행렬
   n, m = map(int, input().split())
   
   matrix = [list(map(int, input().split())) for _ in range(n)]
   ```


<br/>

## 3. 순회

1. 이중 for문을 이용한 **행 우선 순회**

   ```python
   matrix = [
       [1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 0, 1, 2]
   ]
   
   for i in range(3):
       for j in range(4):
           print(matrix[i][j], end=" ")
       print()
   # 1 2 3 4
   # 5 6 7 8
   # 9 0 1 2
   ```

2. 이중 for문을 이용한 **열 우선 순회**

   ```python
   matrix = [
       [1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 0, 1, 2]
   ]
   
   for i in range(3):
       for j in range(4):
           print(matrix[j][i], end=" ")
       print()
   # 1 5 9
   # 2 6 0
   # 3 7 1
   # 4 8 2
   ```

3. Pythonic한 방법으로 이차원 리스트 총합 구하기

   ```python
   matrix = [
       [1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 0, 1, 2]
   ]
   
   total = sum(map(sum, matrix))
   
   print(total)
   # 48
   ```

4. 행 우선 순회를 이용해 이차원 리스트의 최댓값, 최솟값 구하기

   ```python
   matrix = [
       [1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 0, 1, 2]
   ]
   
   max_value = 0
   
   for i in range(3):
       for j in range(4):
           if matrix[i][j] > max_value:
               max_value = matrix[i][j]
   
   print(max_value)
   # 9
   
   ############################
   
   max_value = max(map(max, matrix))
   ```

   ```python
   matrix = [
       [1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 0, 1, 2]
   ]
   
   min_value = 0
   
   for i in range(3):
       for j in range(4):
           if matrix[i][j] < min_value:
               min_value = matrix[i][j]
   
   print(min_value)
   # 0
   
   ############################
   
   min_value = min(map(min, matrix))
   ```

<br/>

## 4. 전치

> 전치(transpose)란 행렬의 행과 열을 서로 맞바꾸는 것을 의미한다.

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

trans_matrix = [[0] * 3 for _ in range(4)]

for i in range(4):
    for j in range(3):
        trans_matrix[i][j] = matrix[j][i]

print(trans_matrix)
# [[1, 5, 9], [2, 6, 0], [3, 7, 1], [4, 8, 2]]
```

<br/>

## 5. 회전

> 문제에서 이차원 리스트를 왼쪽, 오른쪽으로 90도 회전하는 경우가 존재한다.

1. 왼쪽으로 90도 회전하기

   ```python
   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]
   
   n = 3
   rotated_matrix = [[0] * n for _ in range(n)]
   
   for i in range(n):
       for j in range(n):
           rotated_matrix[i][j] = matrix[j][n-i-1]
   ```

2. 오른쪽으로 90도 회전하기

   ```python
   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]
   
   n = 3
   rotated_matrix = [[0] * n for _ in range(n)]
   
   for i in range(n):
       for j in range(n):
           rotated_matrix[i][j] = matrix[n-j-1][i]
   ```

   
