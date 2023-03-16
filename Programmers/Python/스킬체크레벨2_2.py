def solution(n, k):
    answer = 0
    change = ""

    while True:
        if n >= k:
            change += str(n % k)
        else:
            if n:
                change += str(n)
                break
            else:
                break

        n //= k

    change = change[::-1]
    nums = change.split("0")

    for num in nums:
        if num:
            num = int(num)
            flag = True

            if num > 1:
                for i in range(2, int(num ** (1 / 2)) + 1):
                    if num % i == 0:
                        flag = False
                        break

                if flag:
                    answer += 1

    return answer


print(solution(8, 3))
print(solution(437674, 3))
print(solution(110011, 10))
