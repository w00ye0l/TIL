from itertools import permutations


def solution(ability):
    answer = 0

    i = len(ability)
    j = len(ability[0])

    num = [i for i in range(1, i + 1)]
    mem = list(set(permutations(num, j)))

    score = []
    for m in mem:
        sum_ = 0

        for c in range(len(m)):
            sum_ += ability[m[c] - 1][c]

        score.append(sum_)

    answer = max(score)

    return answer


print(solution([[40, 10, 10], [20, 5, 0], [
      30, 30, 30], [70, 0, 70], [100, 100, 100]]))
