n = int(input())


def bfs(i, j, n):
    global result
    sum_ = 0
    for x in range(i, i + n):
        for y in range(j, j + n):
            sum_ += video[x][y]

    if sum_ == n**2:
        result += "1"
    elif sum_ == 0:
        result += "0"
    else:
        result += "("
        bfs(i, j, n // 2)
        bfs(i, j + n // 2, n // 2)
        bfs(i + n // 2, j, n // 2)
        bfs(i + n // 2, j + n // 2, n // 2)
        result += ")"


video = []
for _ in range(n):
    video.append(list(map(int, input())))

result = ""
bfs(0, 0, n)

print(result)
