import sys

INF = sys.maxsize

n = int(input())

material = []

for _ in range(n):
    material.append(list(map(int, input().split())))

visited = [0 for _ in range(n)]

answer = INF


def makeFood(idx):
    global answer

    if idx == len(material):
        cnt, s, b = 0, 1, 0

        for i in range(len(visited)):
            if visited[i]:
                cnt += 1
                s *= material[i][0]
                b += material[i][1]

        if cnt == 0:
            return

        answer = min(answer, abs(s - b))
        return answer

    visited[idx] = 1
    makeFood(idx + 1)
    visited[idx] = 0
    makeFood(idx + 1)


makeFood(0)

print(answer)
