def solution(progresses, speeds):
    answer = []

    while progresses:
        l = len(progresses)
        cnt = 0

        for i in range(l):
            progresses[i] += speeds[i]

        i = 0
        while i < l:
            i += 1
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1

        if cnt != 0:
            answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
