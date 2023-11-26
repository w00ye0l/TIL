N = int(input())

words = [input() for _ in range(N)]
alpha = [0] * 26
answer = 0

for word in words:
    temp = 1
    for j in range(len(word) - 1, -1, -1):
        alpha[ord(word[j]) - ord("A")] += temp
        temp *= 10

alpha.sort(reverse=True)

for i in range(10):
    answer += alpha[i] * (9 - i)

print(answer)
