from collections import deque


def NextGear(x, direction):
    if not visited[x][0]:
        visited[x] = [1, direction]

    if x != 1:
        if gear[x][6] != gear[x - 1][2] and not visited[x - 1][0]:
            visited[x - 1] = [1, direction * -1]
            NextGear(x - 1, direction * -1)
    if x != 4:
        if gear[x][2] != gear[x + 1][6] and not visited[x + 1][0]:
            visited[x + 1] = [1, direction * -1]
            NextGear(x + 1, direction * -1)


def Turn(x, direction):
    if direction == -1:
        gear[x].append(gear[x].popleft())
    else:
        gear[x].appendleft(gear[x].pop())


# 톱니바퀴 입력
gear = [deque()]
for _ in range(4):
    gear.append(deque(map(int, input())))

# 회전 횟수 입력
k = int(input())

# 회전 방법 입력
for _ in range(k):
    x, direction = map(int, input().split())

    # 하나의 회전으로 돌아가는 톱니바퀴 체크
    visited = [[0, 0] for _ in range(5)]

    # 톱니바퀴 회전 체크
    NextGear(x, direction)

    # 돌아가는 톱니바퀴 모두 회전
    for i in range(1, 5):
        if visited[i][0]:
            Turn(i, visited[i][1])

# 점수 구하기
answer = 0
for i in range(1, 5):
    if gear[i][0] == 1:
        answer += 2 ** (i - 1)

print(answer)
