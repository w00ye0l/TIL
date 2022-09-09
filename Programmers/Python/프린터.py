def solution(priorities, location):
    answer = 0
    idx = [i for i in range(len(priorities))]
    result = []

    while priorities:
        max_ = max(priorities)
        cur = priorities.pop(0)

        if cur == max_:
            cur_idx = idx.pop(0)
            result.append(cur_idx)
        else:
            priorities.append(cur)
            idx.append(idx.pop(0))

    answer = result.index(location) + 1

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))
