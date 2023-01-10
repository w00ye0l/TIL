import sys

input = sys.stdin.readline

n, k, s = map(int, input().split())

left_apt, right_apt = [], []

for _ in range(n):
    a, b = map(int, input().split())

    if a < s:
        left_apt.append([s - a, b])
    else:
        right_apt.append([a - s, b])

left_apt = sorted(left_apt, key=lambda x: x[0])
right_apt = sorted(right_apt, key=lambda x: x[0])


def solution(arr):
    result, stu, temp = 0, k, []

    while arr:
        cur = arr.pop()

        if stu >= cur[1]:
            stu -= cur[1]
        else:
            arr.append((cur[0], cur[1] - stu))
            stu = 0

        temp.append(cur[0])

        if stu == 0 or not arr:
            result += max(temp) * 2
            stu, temp = k, []

    return result


print(solution(left_apt) + solution(right_apt))
