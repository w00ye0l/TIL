N = int(input())
arr = list(map(int, input().split()))


def solution():
    # 뒤에서부터 내림차순 시작점 찾기
    i = N - 1
    while i > 0 and arr[i - 1] > arr[i]:
        i -= 1

    # 이미 모두 내림차순이라면 마지막 순열
    if i <= 0:
        return False

    # 뒤에서부터 내림차순 시작점 전 수보다 큰 수 찾기
    j = N - 1
    while arr[j] < arr[i - 1]:
        j -= 1

    # 내림차순 시작점 전 수와 다음에 차례 수 바꾸기
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    # 내림차순이었던 리스트 뒤집어서 오름차순으로
    arr[i:] = arr[i:][::-1]

    return True


if solution():
    print(*arr)
else:
    print(-1)
