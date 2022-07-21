t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = [2, 3, 5, 7, 11]
    result = []

    for num in arr:
        cnt = 0
        while n % num == 0:
            cnt += 1
            n //= num
        result.append(str(cnt))

    answer = ' '.join(result)
    print(f'#{i} {answer}')
