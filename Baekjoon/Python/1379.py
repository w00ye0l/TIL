import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

course = []
class_ = []
classNum = [0] * N
answer = 0

for _ in range(N):
    num, s, e = map(int, input().split())
    course.append((s, e, num - 1))

course.sort()

for s, e, num in course:
    if class_ and class_[0][0] <= s:
        classNum[num] = classNum[class_[0][2]]
        heappop(class_)
    else:
        answer += 1
        classNum[num] = answer

    heappush(class_, (e, s, num))

print(answer)
print(*classNum, sep="\n")
