arr = []
s = 0
for i in range(302):
    s += i
    arr.append(s)

T = int(input())

for _ in range(T):
    n = int(input())

    answer = 0

    for i in range(1, n + 1):
        answer += i * arr[i + 1]

    print(answer)
