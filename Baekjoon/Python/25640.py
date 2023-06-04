MBTI = input()

N = int(input())

cnt = 0

for _ in range(N):
    if input() == MBTI:
        cnt += 1

print(cnt)
