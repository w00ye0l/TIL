import sys

input = sys.stdin.readline


def cal():
    global answer

    a = (visited[0][0] - visited[1][0]) ** 2 + (visited[0][1] - visited[1][1]) ** 2
    b = (visited[1][0] - visited[2][0]) ** 2 + (visited[1][1] - visited[2][1]) ** 2
    c = (visited[2][0] - visited[0][0]) ** 2 + (visited[2][1] - visited[0][1]) ** 2

    if a + b == c or a + c == b or b + c == a:
        answer += 1


def bt(cnt, start):
    if cnt == 3:
        cal()
        return

    for i in range(start, n):
        visited[cnt] = node[i]
        bt(cnt + 1, i + 1)


n = int(input())

node = []
answer = 0
visited = [0] * 3

for _ in range(n):
    node.append(tuple(map(int, input().split())))

bt(0, 0)

print(answer)
