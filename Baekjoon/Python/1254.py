S = input()
N = len(S)
answer = float("inf")

for i in range(N, -1, -1):
    T = S + S[:i][::-1]
    M = len(S[:i])
    C = (N + M) // 2

    if (N + M) % 2 == 0:
        if T[:C] == T[C:][::-1]:
            answer = min(answer, N + M)
    else:
        if T[:C] == T[C + 1 :][::-1]:
            answer = min(answer, N + M)

print(answer)
