N = int(input())

arr = list(input())
arr.reverse()

nums = []

for _ in range(N):
    nums.append(int(input()))

stack = []

while arr:
    temp = arr.pop()

    if temp.isalpha():
        stack.append(nums[ord(temp) - ord("A")])
    else:
        second = stack.pop()
        first = stack.pop()

        stack.append(eval(str(first) + temp + str(second)))

print(f"{stack[0]:.2f}")
