while True:
    n = int(input())

    if n == 0:
        break
    
    answer = 0
    for i in range(1, n + 1):
        answer += i

    print(answer)