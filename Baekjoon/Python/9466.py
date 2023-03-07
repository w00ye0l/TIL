import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(n):
    global cnt

    visited[n] = 1
    done.append(n)

    if visited[arr[n]]:
        if arr[n] in done:
            cnt += len(done[done.index(arr[n]) :])
    else:
        dfs(arr[n])


for _ in range(int(input())):
    n = int(input())
    cnt = 0
    arr = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if visited[i]:
            continue

        done = []
        dfs(i)

    print(n - cnt)
