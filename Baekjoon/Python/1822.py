nA, nB = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

answer = list(A - B)
answer.sort()

print(len(answer))
print(*answer)
