import sys

sys.setrecursionlimit(10**6)


def dfs(s1, e1, s2, e2):
    if s1 > e1 or s2 > e2:
        return

    root = post_order[e2]

    left = pre_order[root] - s1
    right = e1 - pre_order[root]

    print(root, end=" ")

    dfs(s1, s1 + left - 1, s2, s2 + left - 1)
    dfs(e1 - right + 1, e1, e2 - right, e2 - 1)


n = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pre_order = [0] * (n + 1)

for i in range(n):
    pre_order[in_order[i]] = i

dfs(0, n - 1, 0, n - 1)
