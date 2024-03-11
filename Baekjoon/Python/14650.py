def bt(cur):
    global answer

    if cur != 0:
        if len(str(cur)) == N:
            if cur % 3 == 0:
                answer += 1
        else:
            for num in nums:
                bt(cur * 10 + num)


N = int(input())
nums = [0, 1, 2]
answer = 0

for num in nums:
    bt(num)

print(answer)
