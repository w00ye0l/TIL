N, M, K = map(int, input().split())

w = N // 2
m = M
answer = min(w, m, (N + M - K) // 3)

print(answer)
