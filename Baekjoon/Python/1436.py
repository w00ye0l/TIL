n = int(input())

i = 0
cnt = 0
while cnt != n:             # 666이 들어간 영화 제목이 n번째일 때 종료
    i += 1

    if '666' in str(i):     # 영화 제목에 666이 들어가면
        cnt += 1            # 몇 번째인지 늘려준다
        print(i, cnt)

print(i)
