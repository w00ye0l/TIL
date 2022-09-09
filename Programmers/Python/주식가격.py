def solution(prices):
    answer = []
    len_ = len(prices)

    for i in range(len_):
        cnt = 0
        for j in range(i + 1, len_):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break

        answer.append(cnt)

    return answer


print(solution([1, 2, 3, 2, 3]))
