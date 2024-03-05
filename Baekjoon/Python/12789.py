N = int(input())
arr = list(map(int, input().split()))

get = [0]
wait = [N + 1]

for i in range(N):
    if arr[i] == get[-1] + 1:
        get.append(arr[i])
    else:
        wait.append(arr[i])

    while wait:
        if wait[-1] == get[-1] + 1:
            w = wait.pop()
            get.append(w)
        else:
            break

print("Nice") if not wait else print("Sad")
