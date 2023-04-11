import sys

input = sys.stdin.readline


def cal():
    global answer

    n1, n2, n3 = visited[0], visited[1], visited[2]
    a = (n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2
    b = (n2[0] - n3[0]) ** 2 + (n2[1] - n3[1]) ** 2
    c = (n3[0] - n1[0]) ** 2 + (n3[1] - n1[1]) ** 2

    if 2 * max(a, b, c) == a + b + c:
        answer += 1


def bt(cnt, start):
    if cnt == 3:
        return cal()

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
