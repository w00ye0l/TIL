arr = []
len_ = []
result = []

for i in range(5):
    s = input()
    arr.append(list(s))
    len_.append(len(s))

max_ = max(len_)

for i in range(max_):
    for j in range(5):
        if i < len_[j]:
            result.append(arr[j][i])

print(''.join(result))
