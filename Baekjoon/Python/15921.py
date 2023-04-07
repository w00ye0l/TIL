n = int(input())

if n == 0:
    print("divide by zero")
else:
    score = list(map(int, input().split()))

    avg = sum(score) / n
    expectation = 0

    for i in range(n):
        expectation += score[i] / n

    print("%.2f" % (avg / expectation))
