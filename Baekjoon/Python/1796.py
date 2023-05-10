def solve(x, now, cnt):
    global answer

    if x == 26:
        if answer > cnt:
            answer = cnt
        return

    min_idx = idx[x][0]
    max_idx = idx[x][1]

    if min_idx == max_idx:
        solve(x + 1, max_idx, cnt + abs(now - min_idx) + abs(max_idx - min_idx))
    elif max_idx != -1:
        solve(x + 1, max_idx, cnt + abs(now - min_idx) + abs(max_idx - min_idx))
        solve(x + 1, min_idx, cnt + abs(now - max_idx) + abs(min_idx - max_idx))
    else:
        solve(x + 1, now, cnt)


s = list(input())

idx = [[float("inf"), -1] for _ in range(26)]
answer = float("inf")

for i in range(26):
    for j in range(len(s)):
        if s[j] == chr(i + ord("a")):
            idx[i][0] = min(idx[i][0], j)
            idx[i][1] = max(idx[i][1], j)

solve(0, 0, 0)

print(answer + len(s))
