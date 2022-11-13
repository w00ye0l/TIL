def divisor(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1

    return cnt


for _ in range(int(input())):
    answer = 0
    n = int(input())

    for i in range(1, n + 1):
        if divisor(i) % 2 == 1:
            answer += 1

    print(answer)
