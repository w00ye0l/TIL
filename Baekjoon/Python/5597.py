arr = [0 for _ in range(31)]
arr[0] = 1

for _ in range(28):
    arr[int(input())] += 1

for i in range(31):
    if arr[i] == 0:
        print(i)
