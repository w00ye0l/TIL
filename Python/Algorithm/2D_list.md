# 이차원 리스트

> 이차원 리스트는 리스트를 원소로 가지는 리스트일 뿐이다.
>
> `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
>
> 이차원 리스트는 행렬(matrix)이다.

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

1. 행렬의 크기가 미리 주어지는 경우

   ```python
   # 3 X 3 행렬
   matrix = [list(map(int, input().split())) for _ in range(3)]
   ```

2. 행렬의 크기가 입력으로 주어지는 경우

   ```python
   # n X m 행렬
   n, m = map(int, input().split())
   
   matrix = [list(map(int, input().split())) for _ in range(n)]
   ```

   

