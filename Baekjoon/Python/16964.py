import sys

input = sys.stdin.readline


def dfs(x):
    if check[x]:
        return

    check[x] = 1
    answer.append(x)

    for adj in node[x]:
        if not check[adj]:
            dfs(adj)

    check[x] = 0


N = int(input())

node = [[] for _ in range(N + 1)]
check = [0 for _ in range(N + 1)]
answer = []

for _ in range(N - 1):
    s, e = map(int, input().split())

    node[s].append(e)
    node[e].append(s)

arr = list(map(int, input().split()))
dic = {}
for i in range(N):
    dic[arr[i]] = i

for i in range(1, N + 1):
    node[i].sort(key=lambda x: dic[x])

dfs(1)

if answer == arr:
    print(1)
else:
    print(0)
