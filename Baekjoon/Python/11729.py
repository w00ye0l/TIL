n = int(input())


# 하노이 탑을 이동 시킬 함수
def hanoi(n, start, sub, end):
    # n이 1인 마지막의 경우
    if n == 1:
        # 이동을 출력하고 종료
        print(start, end)
        return

    # 제일 큰 원판인 n번 원판을 제외한 n - 1개의 원판을 end를 거쳐 sub에 이동
    hanoi(n - 1, start, end, sub)
    # 제일 큰 n번 원판을 end로 이동하면서 출력
    print(start, end)
    # n - 1개의 원판을 다시 start를 거처 end로 이동
    hanoi(n - 1, sub, start, end)


# 하노이 탑의 이동 횟수는 2**n - 1
print(pow(2, n) - 1)
# n개의 원판을 1, 2, 3번의 기둥을 가지고 이동
hanoi(n, 1, 2, 3)
