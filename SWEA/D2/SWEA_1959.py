t = int(input())
n_arr = []
m_arr = []

for i in range(1, t+1):
    n, m = map(int, input().split())
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))
    max_ = 0

    if n < m:
        for j in range(m - n + 1):
            sum_ = 0
            for k in range(n):
                sum_ += n_arr[k] * m_arr[j + k]
            if max_ < sum_:
                max_ = sum_
    else:
        for j in range(n - m + 1):
            sum_ = 0
            for k in range(m):
                sum_ += n_arr[j + k] * m_arr[k]
            if max_ < sum_:
                max_ = sum_

    print(f'#{i} {max_}')
