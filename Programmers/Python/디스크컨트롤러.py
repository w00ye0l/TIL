import heapq


def solution(jobs):
    answer = 0

    heap = []
    result = []
    start, end = -1, 0

    while len(result) != len(jobs):
        for j in jobs:
            if start < j[0] <= end:
                heapq.heappush(heap, (j[1], j[0]))

        if heap:
            cur = heapq.heappop(heap)
            start = end
            end += cur[0]

            result.append(end - cur[1])
        else:
            end += 1

    answer = int(sum(result) / len(jobs))

    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))
