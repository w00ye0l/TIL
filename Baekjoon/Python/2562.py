arr = []
max = 0
max_idx = 1

for i in range(9):
    arr.append(int(input()))

for j in range(9):
    if max < arr[j]:
        max = arr[j]
        max_idx = j

print(max)
print(max_idx+1)
