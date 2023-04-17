h, n = map(int, input().split())

dis = max(h, n) - min(h, n) + 1
visited = [[0] * dis for _ in range(dis)]
visited[0][0] = 1

for i in range(1, dis):
    for j in range(i + 1):
        visited[i][j] = visited[i - 1][j] + visited[i][j - 1]

print(visited[-1][-1])
