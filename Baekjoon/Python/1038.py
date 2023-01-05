from collections import deque

dp = [0] * 1000001
queue = deque()

n = int(input())

for i in range(1, 10):
    queue.append(i)
    dp[i] = i

if n <= 10:
    # 10 이하는 그냥 출력
    print(n)
else:
    # 최대 길이는 10 => 9876543210 보다 큰 감소하는 수는 없음
    idx = 10

    # queue에서 가장 작은 수를 빼면서 뒤에 숫자를 늘리고 다시 추가
    while idx <= n and queue:
        num = queue.popleft()

        last = num % 10
        # 마지막 수보다는 추가되는 수가 작아야 함
        for i in range(last):
            queue.append(num * 10 + i)
            # idx는 감소하는 수의 인덱스
            dp[idx] = num * 10 + i
            idx += 1

    if dp[n] != 0:
        print(dp[n])
    else:
        print(-1)
