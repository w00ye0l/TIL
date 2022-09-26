def dfs(n):
    if n in dic:
        return dic[n]

    dic[n] = dfs(n // p) + dfs(n // q)

    return dic[n]


n, p, q = map(int, input().split())

dic = {0: 1}

print(dfs(n))
