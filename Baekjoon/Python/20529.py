for _ in range(int(input())):
    N = int(input())

    arr = list(input().split())

    if N > 32:
        print(0)
        continue
    else:
        answer = float("inf")
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    temp = 0
                    for l in range(4):
                        if arr[i][l] != arr[j][l]:
                            temp += 1
                        if arr[j][l] != arr[k][l]:
                            temp += 1
                        if arr[k][l] != arr[i][l]:
                            temp += 1

                    answer = min(answer, temp)

        print(answer)
