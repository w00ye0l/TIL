n = int(input())

arr = list(map(int, input().split()))

s = int(input())

for i in range(n):
    # 움직일 수 있는 범위에서 최댓값과 그 위치를 저장해야 함
    max_idx, max_ = -1, -1

    # 움직일 수 있는 범위까지 회전
    for j in range(i, i + s + 1):
        # 최대 길이를 넘으면 안됨
        if j >= n:
            break

        # 최댓값 교체, 위치 저장
        if max_ < arr[j]:
            max_ = arr[j]
            max_idx = j

    # 최댓값에서부터 시작 위치까지 역순으로 돌면서 자리 변경
    for j in range(max_idx, i, -1):
        arr[j - 1], arr[j] = arr[j], arr[j - 1]

        # 횟수 하나씩 차감
        s -= 1

    # 횟수를 모두 소진했을 경우 종료
    if s <= 0:
        break

print(*arr)
