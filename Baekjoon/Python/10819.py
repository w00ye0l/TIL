def cal(arr):
    result = 0

    for i in range(n - 1):
        result += abs(arr[i] - arr[i + 1])

    return result


def bt(cnt, temp):
    global answer

    if cnt == n:
        answer = max(answer, cal(temp))
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            temp.append(arr[i])

            bt(cnt + 1, temp)

            visited[i] = 0
            temp.pop()


n = int(input())
arr = list(map(int, input().split()))

visited = [0] * n
answer = 0

bt(0, [])

print(answer)
