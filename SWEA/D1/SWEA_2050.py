s = list(input())
arr = []

for i in s:
    arr.append(str(ord(i)-64))

print(' '.join(arr))
