def solution(numbers):
    answer = ''

    num = list(map(str, numbers))

    num.sort(key=lambda x: x * 3, reverse=True)

    answer = ''.join(num)

    return str(int(answer))


print(solution([0, 0, 0]))
