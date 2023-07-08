N = int(input())

answer = 0
for _ in range(N):
    emo = input()

    day = int(emo[2:])

    if day <= 90:
        answer += 1

print(answer)
