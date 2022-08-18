n, l = map(int, input().split())

fruit = list(map(int, input().split()))

visited = [0] * (n)

while True:
    cnt = 0
    if not 0 in visited:
        break

    for i in range(n):
        if l >= fruit[i] and visited[i] == 0:
            cnt += 1
            l += 1
            visited[i] = 1

    if cnt == 0:
        break

print(l)
