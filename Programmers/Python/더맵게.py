import heapq


def solution(scoville, K):
    answer = 0

    scoville.sort()

    while True:
        chk = heapq.heappop(scoville)

        if chk >= K:
            break
        else:
            heapq.heappush(scoville, chk)

        if len(scoville) < 2:
            answer = -1
            break
        else:
            p1 = heapq.heappop(scoville)
            p2 = heapq.heappop(scoville)

            heapq.heappush(scoville, (p1 + (p2 * 2)))
            answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
