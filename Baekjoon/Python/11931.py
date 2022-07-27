import sys
input = sys.stdin.readline
# 입력이 많아서 시간 초과 발생..

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

for i in sorted(arr, reverse=True):
    print(i)
