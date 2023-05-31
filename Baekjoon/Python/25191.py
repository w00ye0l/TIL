N = int(input())
A, B = map(int, input().split())

print(min(A // 2 + B, N))
