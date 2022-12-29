def solution(ingredient):
    answer = 0

    i = 0
    while len(ingredient) - 3 > i:
        if ingredient[i] == 1:
            if ingredient[i : i + 4] == [1, 2, 3, 1]:
                del ingredient[i : i + 4]
                i -= 3
                answer += 1
                continue

        i += 1

    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))
