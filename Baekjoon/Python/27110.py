N = int(input())
A, B, C = map(int, input().split())

print(min(A, N) + min(B, N) + min(C, N))
