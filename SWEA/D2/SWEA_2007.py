t = int(input())

for i in range(1, t+1):
    arr = list(input())
    result = 0
    for j in range(1, 30):
        if arr[j] == arr[0] and arr[j+1] == arr[1]:
            result = j
            break
    print(f'#{i} {result}')
