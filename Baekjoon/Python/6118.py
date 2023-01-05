import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 연결된 헛간 그래프
graph = [[] for _ in range(n + 1)]
# 방문 처리 리스트
visited = [-1 for _ in range(n + 1)]

# 양방향 연결 그래프
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


# BFS로 탐색
def bfs(n):
    queue = deque()
    queue.append(n)
    visited[n] = 0

    # 1번부터 들어간 후
    while queue:
        # 현재 노드를 꺼내고
        cur = queue.popleft()

        # 현재 노드와 연결된 노드를 탐색
        for adj in graph[cur]:
            # 연결된 노드가 아직 방문하지 않았다면
            if visited[adj] == -1:
                # queue에 넣고
                queue.append(adj)
                # 거리를 1 증가시켜 방문 처리
                visited[adj] = visited[cur] + 1


# 1번부터 탐색
bfs(1)

# 가장 먼 거리에 있는 노드의 위치를 탐색
# index()의 경우 가장 먼저 만나는 곳을 저장
print(
    # 가장 먼 거리의 헛간 위치
    visited.index(max(visited)),
    # 가장 먼 거리
    max(visited),
    # 가장 먼 거리의 헛간 개수
    visited.count(max(visited)),
)
