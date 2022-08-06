n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

numbers.sort()
left, right = 0, n - 1
cnt = 0

while left != right:
    if numbers[left] + numbers[right] == x:
        left += 1
        cnt += 1
    elif numbers[left] + numbers[right] > x:
        right -= 1
    else:
        left += 1

print(cnt)
