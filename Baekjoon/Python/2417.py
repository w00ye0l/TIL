n = int(input())

start, end = 0, n
result = 0

while start <= end:
    q = (start + end) // 2

    # q의 제곱값이 입력값보다 작은 경우 답이 될 수 없음
    if q**2 < n:
        start = q + 1
    # q의 제곱값이 입력값보다 크거나 같은 경우 result에 값을 넣고 최소를 찾음
    else:
        result = q
        end = q - 1

    print(start, end, result)

print(result)
