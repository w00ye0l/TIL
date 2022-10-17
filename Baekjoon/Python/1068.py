def dfs(cut, tree):
    tree[cut] = -2

    for i in range(len(tree)):
        if cut == tree[i]:
            print(i, tree[i])
            dfs(i, tree)


n = int(input())
tree = list(map(int, input().split()))
cut = int(input())
cnt = 0

dfs(cut, tree)

for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)
