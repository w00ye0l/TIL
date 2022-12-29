def solution(arr):
    answer = []
    arr.pop(arr.index(min(arr)))

    if arr:
        answer = arr
    else:
        answer = [-1]

    return answer


print(solution([4, 3, 2, 1]))
print(solution([10]))
print(solution([4, 2, 3, 3, 1, 1]))
