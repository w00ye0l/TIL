P = int(input())

for _ in range(P):
    T, *arr = map(int, input().split())
    answer = 0

    for i in range(20):
        for j in range(i):
            if arr[j] > arr[i]:
                answer += i - j

                pick = arr.pop(i)
                arr.insert(j, pick)

                break

    print(T, answer)
