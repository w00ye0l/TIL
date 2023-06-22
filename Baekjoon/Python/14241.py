N = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0

while len(arr) > 1:
    x = arr.pop()
    y = arr.pop()

    answer += x * y

    arr.append(x + y)

print(answer)
