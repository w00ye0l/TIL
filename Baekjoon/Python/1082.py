def solution():
    n = int(input())
    cost = list(map(int, input().split()))
    money = int(input())

    spend, idx = 0, 0
    result = [0 for _ in range(51)]
    min_idx = cost.index(min(cost))

    # 0이 가장 싼 값이라면
    if min_idx == 0:
        # n이 1이 아니라면
        if n != 1:
            # 두 번째로 가장 싼 값을 탐색
            min_idx = cost.index(min(cost[1:]))
            # 두 번째로 가장 싼 수를 살 수 없다면
            if cost[min_idx] > money:
                # 0만 살 수 있으므로 0 출력 후 종료
                print(0)
                return
            # 살 수 있다면 두 번째로 가장 싼 값을 맨 앞에 저장 후 다시 0으로 교체
            else:
                result[idx] = min_idx
                spend += cost[min_idx]
                idx += 1
                min_idx = 0

    # 가진 돈으로 살 수 있는 수를 계속 누적
    while spend + cost[min_idx] <= money:
        result[idx] = min_idx
        spend += cost[min_idx]
        idx += 1

    # 저장된 결과에서 맨 앞부터 큰 수부터 역순으로 비교하여 큰 숫자로 교체
    for i in range(idx):
        for j in range(n - 1, -1, -1):
            # 사용한 돈 - 현재 사용한 돈 + 교체해서 사용할 돈 <= 가진 돈
            if spend - cost[result[i]] + cost[j] <= money:
                spend = spend - cost[result[i]] + cost[j]
                result[i] = j
                break

    for i in range(idx):
        print(result[i], end="")


solution()
