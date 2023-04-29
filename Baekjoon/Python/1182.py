def bt(idx):
    global answer

    if len(visited) > 0 and sum(visited) == s:
        answer += 1

    for i in range(idx, n):
        visited.append(arr[i])
        bt(i + 1)
        visited.pop()


n, s = map(int, input().split())

arr = list(map(int, input().split()))
visited = []
answer = 0

bt(0)

print(answer)
