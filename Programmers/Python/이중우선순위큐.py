import heapq


def solution(operations):
    answer = []

    heap = []
    for o in operations:
        order, num = list(o.split())

        if order == 'I':
            heapq.heappush(heap, int(num))

        elif order == 'D':
            if int(num) == -1:
                if heap:
                    heapq.heappop(heap)
            else:
                if heap:
                    heap.pop()
                    heapq.heapify(heap)

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer.append(0)
        answer.append(0)

    return answer


print(solution(["I -45", "I 653", "D 1", "I -642",
      "I 45", "I 97", "D 1", "D -1", "I 333"]))
