from itertools import permutations


def solution(numbers):
    answer = 0
    number = list(numbers)

    pd = set()
    for i in range(1, len(number) + 1):
        for j in list(set(permutations(number, i))):
            pd.add(int(''.join(j)))

    for p in pd:
        if p == 0:
            continue

        cnt = 0
        for i in range(1, p // 2 + 1):
            if p % i == 0:
                cnt += 1

        if cnt == 1:
            answer += 1

    return answer


print(solution("011"))
