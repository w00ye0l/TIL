n = int(input())

seat = {}
cnt = 0

want_seat = list(map(int, input().split()))

for i in range(n):
    if want_seat[i] not in seat:
        seat[want_seat[i]] = 1
    else:
        cnt += 1

print(cnt)
