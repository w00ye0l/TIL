import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

stack = []
nge = [-1] * n                          # 결과의 default == -1

for i in range(n):
    while stack:                        # 스택이 있으면
        if num[i] > num[stack[-1]]:     # 스택의 마지막 값과 i를 인덱스로 가지는 배열의 값 비교
            nge[stack.pop()] = num[i]   # 스택의 마지막 값을 인덱스로 가지는 결과에 배열값 저장
        else:                           # 리스트의 값이 다음 값보다 크면
            break                       # 커지는 값을 찾을 때까지 스택에 저장

    stack.append(i)                     # 스택에 i 저장, 처음엔 0이 저장됨

print(*nge)
