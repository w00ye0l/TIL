n = int(input())

m = int(input())

num = list(map(int, input().split()))
num.sort()

cnt = 0
start = 0
end = n - 1

while True:
    if start >= end:
        break

    if num[start] + num[end] == m:
        start += 1
        end -= 1
        cnt += 1
    elif num[start] + num[end] < m:
        start += 1
    else:
        end -= 1

print(cnt)
