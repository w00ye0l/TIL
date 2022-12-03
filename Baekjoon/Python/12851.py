from collections import deque

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]

min_, result = -1, 0


def bfs(n, k):
    global result, min_

    queue = deque()
    queue.append((n, 0))
    visited[n] = 1

    while queue:
        (cur, t) = queue.popleft()
        visited[cur] = 1

        # 최소 이동 시간이 있고 queue에서 나온 값이 최소보다 크면 바로 종료
        if t > min_ and min_ != -1:
            return

        # queue에서 꺼낸 값들을 목표 위치와 비교하고
        # 최소 시간이 -1이라면 최소 시간 갱신, 방법 추가
        if min_ == -1 and cur == k:
            min_ = t
            result += 1
        # 최소 시간이 있다면 방법만 추가
        elif min_ != -1 and cur == k:
            result += 1

        # BFS 모든 경우 저장
        # 한 번 간 경우는 또 가지 않음 => visited 확인
        if cur * 2 <= 100000 and not visited[cur * 2]:
            queue.append((cur * 2, t + 1))

        if cur + 1 <= 100000 and not visited[cur + 1]:
            queue.append((cur + 1, t + 1))

        if 0 <= cur - 1 and not visited[cur - 1]:
            queue.append((cur - 1, t + 1))


bfs(n, k)

print(min_)
print(result)
