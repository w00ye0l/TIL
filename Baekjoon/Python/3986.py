N = int(input())

answer = 0

for _ in range(N):
    word = input()

    arr = []

    for i in range(len(word)):
        if not arr:
            arr.append(word[i])

        elif arr[-1] == word[i]:
            arr.pop()
        elif arr[-1] != word[i]:
            arr.append(word[i])

    if not arr:
        answer += 1

print(answer)
