import sys

input = sys.stdin.readline

ans = 0


def b_s(arr, target, start, end):
    global ans
    # 비교의 시작은 첫 집부터
    pre = arr[0]

    if start > end:
        return ans

    # 최대 거리가 될 수 있는 값을 기준으로 탐색
    mid = (start + end) // 2

    # 첫 번째 집은 공유기가 있다고 가정
    cnt = 1
    for i in range(1, n):
        # 두 번째 집부터 그 전에 공유기가 있는 집과의 거리를 계산
        # 거리보다 크거나 같은 집이 있으면
        if house[i] - pre >= mid:
            cnt += 1
            # 공유기 설치 후 비교 대상 바꾸기
            pre = house[i]

    # 만약 공유기가 설치된 집이 공유기 수보다 많거나 같으면 정답에 넣고
    if cnt >= target:
        # 설치된 공유기가 공유기의 수보다 많아도 공유기 수만 설치해도 됨
        ans = max(ans, mid)
        # 거리를 늘려서 다시 탐색
        return b_s(arr, target, mid + 1, end)
    else:
        return b_s(arr, target, start, mid - 1)


n, c = map(int, input().split())

house = []
for _ in range(n):
    house.append(int(input()))

house.sort()

# 최소 거리는 1, 최대 거리는 시작과 끝 거리
print(b_s(house, c, 1, house[-1] - house[0]))
