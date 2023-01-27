n = int(input())

words = []
shortcut = []

for _ in range(n):
    words.append(list(map(list, input().split())))

for i in range(n):
    flag = True
    break_flag = False

    for j in range(len(words[i])):
        if not words[i][j][0].upper() in shortcut:
            shortcut.append(words[i][j][0].upper())
            words[i][j][0] = "[" + words[i][j][0] + "]"
            flag = False
            break

    if flag:
        for j in range(len(words[i])):
            for k in range(len(words[i][j])):
                if not words[i][j][k].upper() in shortcut:
                    shortcut.append(words[i][j][k].upper())
                    words[i][j][k] = "[" + words[i][j][k] + "]"
                    break_flag = True
                    break

            if break_flag:
                break

for i in range(n):
    for j in range(len(words[i])):
        print("".join(words[i][j]), end=" ")
    print()
