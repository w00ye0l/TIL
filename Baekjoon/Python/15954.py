import math
from decimal import *

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = Decimal("inf")

for i in range(N - K + 1):
    # K - 1개까지
    sum_ = sum(arr[i : i + K - 1])
    sum_sq = sum([v * v for v in arr[i : i + K - 1]])

    # 1개 ~ 끝까지 단계별로 더하기
    for l in range(K, N - i + 1):
        sum_ += arr[i + l - 1]
        sum_sq += arr[i + l - 1] ** 2

        avg = sum_ / Decimal(l)

        # 분산은 제곱의 평균 - 평균의 제곱
        # 표준 편차는 분산의 제곱근
        std = math.sqrt(sum_sq / Decimal(l) - avg**2)

        answer = min(answer, std)

print(answer)
