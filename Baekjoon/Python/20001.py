problem = []

while True:
    s = input()

    if s == '고무오리 디버깅 시작':
        pass
    if s == '고무오리 디버깅 끝':
        break

    if s == '문제':
        problem.append(1)
    elif s == '고무오리':
        if len(problem) == 0:
            problem.append(1)
            problem.append(1)
        else:
            problem.pop()

if len(problem) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')
