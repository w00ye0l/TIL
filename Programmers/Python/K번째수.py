def solution(array, commands):
    answer = []

    for c in commands:
        [i, j, k] = c
        temp = array[i - 1:j]

        temp.sort()

        answer.append(temp[k - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
