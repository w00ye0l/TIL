def solution(scores):
    wonho = scores[0]
    wonho_sum = sum(wonho)

    scores.sort(key=lambda x: (-x[0], x[1]))

    max_person, answer = 0, 1

    for score in scores:
        if wonho[0] < score[0] and wonho[1] < score[1]:
            return -1

        if max_person <= score[1]:
            if wonho_sum < score[0] + score[1]:
                answer += 1

            max_person = score[1]

    return answer


print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
