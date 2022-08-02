import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sign = 'Yes'

for i in range(m):
    ki = int(input())
    stack_ = list(map(int, input().split()))

    print(stack_)

    comparison = stack_.pop()

    while len(stack_) != 0:
        if stack_[-1] > comparison:
            comparison = stack_.pop()
        else:
            sign = 'No'
            break

    # for j in range(ki - 1):
    #     if stack_[j] < stack_[j + 1]:
    #         sign = 'No'

print(sign)
