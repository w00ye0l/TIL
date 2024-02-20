while True:
    try:
        N, M = map(int, input().split())
        answer = 0

        for i in range(N, M + 1):
            if len(list(str(i))) == len(set(str(i))):
                answer += 1

        print(answer)
    except:
        break
