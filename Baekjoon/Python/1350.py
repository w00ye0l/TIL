N = int(input())

arr = list(map(int, input().split()))
size = int(input())

answer = 0

for a in arr:
    if a % size:
        answer += (a // size + 1) * size
    else:
        answer += a // size * size

print(answer)
