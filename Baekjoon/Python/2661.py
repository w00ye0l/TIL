def backTracking(idx):
    global answer

    if not answer:
        if idx == n:
            answer = "".join(map(str, arr))
            return

        for i in range(1, 4):
            arr.append(i)
            flag = True

            for j in range(1, len(arr) // 2 + 1):
                if arr[-j:] == arr[-2 * j : -j]:
                    flag = False

            if flag:
                backTracking(idx + 1)

            arr.pop()

    return


n = int(input())

arr = []
answer = ""

backTracking(0)

print(answer)
