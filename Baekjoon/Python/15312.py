cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

A = input()
B = input()

arr = []

for i in range(len(A)):
    arr.append(cnt[ord(A[i]) - ord("A")])
    arr.append(cnt[ord(B[i]) - ord("A")])

while True:
    temp = []

    for i in range(len(arr) - 1):
        temp.append((arr[i] + arr[i + 1]) % 10)

    arr = temp

    if len(arr) == 2:
        break

print(*arr, sep="")
