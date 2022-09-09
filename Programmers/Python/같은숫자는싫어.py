def solution(arr):
    answer = []

    for a in arr:
        if answer == []:
            answer.append(a)

        if a != answer[-1]:
            answer.append(a)

    return answer


print(solution([4, 4, 4, 3, 3]))
