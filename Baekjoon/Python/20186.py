N, K = map(int, input().split())
arr = list(map(int, input().split()))

s_arr = list(reversed(sorted(arr)))
answer = sum(s_arr[:K]) - (K * (K - 1) // 2)

print(answer)
