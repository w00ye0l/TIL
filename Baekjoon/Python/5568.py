from itertools import permutations

n = int(input())
k = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

per = permutations(arr, k)

answer = set()

for p in per:
    answer.add("".join(list(map(str, p))))

print(len(answer))
