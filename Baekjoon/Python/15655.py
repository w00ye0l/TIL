from itertools import compress


def bt(idx):
    if sum(visited) == m:
        print(*list(compress(arr, visited)))

    for i in range(idx, n):
        visited[i] = 1
        bt(i + 1)
        visited[i] = 0


n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
visited = [0] * n

bt(0)
