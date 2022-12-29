def solution(n):
    answer = ""

    watermelon = "수박"
    odd = "수"

    answer += watermelon * (n // 2)

    if n % 2:
        answer += odd

    return answer


print(solution(3))
print(solution(4))
