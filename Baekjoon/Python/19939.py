N, K = map(int, input().split())

if N >= K * (K + 1) // 2:
    if (N - (K * (K + 1) // 2)) % K:
        print(K)
    else:
        print(K - 1)
else:
    print(-1)
