n, m = map(int, input().split())

lamp = []
for _ in range(n):
    lamp.append(list(input()))

k = int(input())

result = 0

for i in range(n):
    off = 0
    # 행마다 열을 돌면서 0의 개수를 파악
    for j in range(m):
        if lamp[i][j] == "0":
            off += 1

    # 각 행의 0의 개수가 k보다 작거나 같고 홀수/짝수가 같은지 판단
    # 홀수일 때 홀수 번 전원을 켜야 모두 불이 켜지고
    # 짝수일 때 짝수 번 전원을 켜야 모두 불이 켜지기 때문
    if off <= k and off % 2 == k % 2:
        cnt = 0
        # 같은 행인 곳은 모두 같이 불이 켜지기 때문에 동시에 켜지는 행 카운트
        for j in range(n):
            if lamp[i] == lamp[j]:
                cnt += 1

        # 모든 경우 중 max 값 출력
        result = max(result, cnt)

print(result)
