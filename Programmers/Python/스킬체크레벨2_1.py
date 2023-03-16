def solution(brown, yellow):
    answer = []
    sum_ = brown + yellow

    for i in range(2, int(sum_ / 2) + 1):
        if sum_ % i == 0:
            a = i
            b = sum_ // i

            if (a - 2) * (b - 2) == yellow:
                answer = [a, b]

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
