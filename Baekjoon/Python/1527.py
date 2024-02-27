def check(num):
    global answer

    if num > B:
        return

    if A <= num <= B:
        answer += 1

    check(num * 10 + 4)
    check(num * 10 + 7)


A, B = map(int, input().split())
answer = 0

check(4)
check(7)

print(answer)
