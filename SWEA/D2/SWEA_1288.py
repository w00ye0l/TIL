t = int(input())

for a in range(1, t+1):
    n = input()     # n을 문자열로 입력 받는다
    temp = n        # n을 그대로 복사해둔다
    result = {}     # 0부터 9까지 들어갈 딕셔너리를 만든다
    cnt = 1         # n에 x번 곱해질 변수를 생성한다

    while len(result) != 10:
        # 딕셔너리의 길이가 10이 되면 멈춘다
        for i in temp:
            if i not in result:
                result[i] = 1
        # 반복문을 돌면서 딕셔너리에 키가 없으면 추가해준다

        cnt += 1
        temp = str(int(temp) + int(n))
        # temp에 n을 계속 더해주며 계산한다

    print(f'#{a} {(cnt - 1) * int(n)}')
    # 최종 딕셔너리의 길이가 10이 되는 수를 구한다
