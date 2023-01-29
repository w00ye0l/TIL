def solution(start, end, flag, arr):
    while start < end:
        if arr[start] != arr[end]:
            if flag:
                if (
                    solution(start + 1, end, 0, arr) == 0
                    or solution(start, end - 1, 0, arr) == 0
                ):
                    return 1
                else:
                    return 2
            else:
                return 2

        start += 1
        end -= 1

    return 0


t = int(input())

for _ in range(t):
    arr = list(input())

    print(solution(0, len(arr) - 1, 1, arr))
