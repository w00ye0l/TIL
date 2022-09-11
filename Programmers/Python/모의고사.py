def solution(answers):
    answer = []

    u1 = [1, 2, 3, 4, 5] * 2000
    u2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    u3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if u1[i] == answers[i]:
            cnt[0] += 1
        if u2[i] == answers[i]:
            cnt[1] += 1
        if u3[i] == answers[i]:
            cnt[2] += 1

    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i + 1)

    return answer


print(solution([1, 3, 2, 4, 2]))
