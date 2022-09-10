from itertools import permutations


def solution(numbers):
    answer = ''
    temp = []

    result = list(permutations(numbers))

    for r in result:
        temp.append(''.join(list(map(str, r))))

    temp.sort()
    answer = temp[-1]

    return answer


print(solution([3, 30, 34, 5, 9]))
