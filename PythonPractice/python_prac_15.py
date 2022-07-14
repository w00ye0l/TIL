# 1)
word = input()

for i in range(len(word)):
    if word[i] == 'a':
        idx = i
        break
    else:
        idx = -1

print(idx)


# 2)
word = input()

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        break
else:
    print(-1)
