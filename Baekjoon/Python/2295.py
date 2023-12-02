import sys

input = sys.stdin.readline


def solution():
    # 가장 큰 수부터 두 수의 차이를 계산해서 남은 두 수의 합을 만들 수 있으면
    # 세 수의 합이 존재하는 것
    # (x + y) = k - z
    for i in range(N - 1, -1, -1):
        for j in range(i, -1, -1):
            num = arr[i] - arr[j]

            if num in sumL:
                return arr[i]


N = int(input())
arr = [int(input()) for _ in range(N)]
sumL = set()

arr.sort()

# 두 수의 합 리스트 생성
for i in range(N):
    for j in range(i, N):
        sumL.add(arr[i] + arr[j])

print(solution())
