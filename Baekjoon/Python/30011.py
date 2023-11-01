N = int(input())

arr = list(map(int, input().split()))

answer = ((arr[0] - 2) + sum(arr[1:])) * 180

print(answer)
