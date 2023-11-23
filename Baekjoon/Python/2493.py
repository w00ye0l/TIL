N = int(input())
arr = list(map(int, input().split()))

answer = [0] * N
stack_ = []

for i in range(N):
    while stack_ and arr[stack_[-1]] < arr[i]:
        stack_.pop()

    if stack_:
        answer[i] = stack_[-1] + 1

    stack_.append(i)

print(answer)
