from collections import defaultdict


def dfs(x):
    stack_ = []
    stack_.append(x)
    visited = [0 for _ in range(n)]
    visited[x] = 1
    for i in range(n):
        if friend[x][i] == "Y":
            stack_.append(i)
            popular[x] += 1
            visited[i] = 1

    while stack_:
        cur = stack_.pop()

        for i in range(n):
            if friend[cur][i] == "Y" and visited[i] == 0:
                popular[x] += 1
                visited[i] = 1


n = int(input())

friend = []

for _ in range(n):
    friend.append(list(input()))


popular = defaultdict(int)
for i in range(n):
    dfs(i)

if popular:
    print(max(popular.values()))
else:
    print(0)
