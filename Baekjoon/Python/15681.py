import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def makeTree(currentNode, parent):
    for node in graph[currentNode]:
        if node != parent:
            if parents[node] == node:
                parents[node] = currentNode
            makeTree(node, currentNode)


def countSubtreeNodes(currentNode):
    size[currentNode] = 1
    for node in graph[currentNode]:
        if node != parents[currentNode]:
            countSubtreeNodes(node)
            size[currentNode] += size[node]


n, r, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]
parents = [i for i in range(n + 1)]
size = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


makeTree(r, -1)

countSubtreeNodes(r)

for _ in range(q):
    u = int(input())

    print(size[u])
