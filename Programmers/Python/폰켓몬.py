def solution(nums):
    answer = 0
    dic = {}

    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1

    len_n = len(nums)
    len_d = len(dic)

    if len_n // 2 >= len_d:
        answer = len_d
    else:
        answer = len_n // 2

    return answer


print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
