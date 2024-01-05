N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
s, e = 0, 0
t = 0

while s < N:
    if t < M and e < N:
        t += arr[e]
        e += 1
    elif t >= M:
        if t == M:
            answer += 1
        t -= arr[s]
        s += 1
    else:
        break

print(answer)
