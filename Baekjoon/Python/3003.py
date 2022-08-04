right = [1, 1, 2, 2, 2, 8]

check = list(map(int, input().split()))

for i in range(len(right)):
    print(right[i] - check[i], end=" ")
