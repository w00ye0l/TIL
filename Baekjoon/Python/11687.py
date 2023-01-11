import sys

INF = sys.maxsize


def binary_search(m):
    start, end = 1, INF
    ans = 0

    while start <= end:
        cnt = 0
        mid = (start + end) // 2

        # 5로 나눈 몫
        # 5의 제곱수는 또 한 번씩 더해줌
        i = 5
        while i <= mid:
            cnt += mid // i
            i *= 5

        if m <= cnt:
            if m == cnt:
                ans = mid

            end = mid - 1
        else:
            start = mid + 1

    if ans:
        return ans
    else:
        return -1


m = int(input())

print(binary_search(m))