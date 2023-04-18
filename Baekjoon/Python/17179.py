n, m, l = map(int, input().split())
s = [int(input()) for _ in range(m)] + [l]
q = [int(input()) for _ in range(n)]


def binarySearch(k):
    start = 1
    end = l
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        temp = 0
        cnt = 0
        for i in range(m + 1):
            if s[i] - temp >= mid:
                temp = s[i]
                cnt += 1

        if cnt > k:
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1

    return answer


for i in range(n):
    print(binarySearch(q[i]))
