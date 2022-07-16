# Python Algorithm Tip(파이썬 알고리즘 팁)

## input()
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