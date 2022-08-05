# Python Algorithm Tip(파이썬 알고리즘 팁)

## 1. input()
> 파이썬 알고리즘 문제를 해결할 때, 입력이 많은 경우 단순 input() 함수는 시간초과를 유발함

### sys.stdin.readline() 사용하기
```python
# 1)
import sys

def input():
    return sys.stdin.readline().rstrip()
# 이 방법을 사용하면 input()을 완전히 바꾸어 사용 가능

##############

# 2)
import sys

input = sys.stdin.readline
# 이 방법을 사용하려면 input().rstrip()을 사용해야 함
# readline()은 뒤에 '\n'인 개행까지 포함하기 때문에 개행을 지워줘야 함
```

<br/>

## 2. 델타 탐색

> 4방위, 8방위 탐색이 필요할 경우 델타 탐색을 사용하면 간편함

```python
# 4방위
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
y, x = 1, 1

for i in range(4):
    yy = y + dy[i]
    xx = x + dx[i]
    print(yy, xx)
    # 0, 1	: 상
    # 2, 1	: 하
    # 1, 0	: 좌
    # 1, 2	: 우
    
# 8방위
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
y, x = 1, 1

for i in range(4):
    yy = y + dy[i]
    xx = x + dx[i]
    print(yy, xx)
    # 0 0
	# 0 1
	# 0 2
	# 1 0
	# 1 2
	# 2 0
	# 2 1
	# 2 2
```

