n, m = map(int, input().split())

lamp = []

for _ in range(n):
    lamp.append(list(map(int, input())))

k = int(input())

result = 0

for i in range(n):
    cnt = 0
    # 행마다 열을 돌면서 0의 개수를 파악
    for j in range(m):
        if lamp[i][j] == 0:
            cnt += 1

    # 각 행의 0의 개수가 k보다 작거나 같고 홀수/짝수가 같은지 판단
    # 홀수일 때 홀수 번 전원을 켜야 모두 불이 켜지고
    # 짝수일 때 짝수 번 전원을 켜야 모두 불이 켜지기 때문
    temp = 0
    if cnt <= k and cnt % 2 == k % 2:
        for j in range(n):
            if lamp[i] == lamp[j]:
                temp += 1

    # 모든 경우 중 max 값 출력
    result = max(result, temp)

print(result)
