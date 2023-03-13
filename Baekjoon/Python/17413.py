s = input()
flag = False
result = []
temp = []

for i in s:
    if i == "<":
        flag = True
        if temp:
            result += temp[::-1]
            temp = []

    elif i == ">":
        result += ">"
        flag = False
        continue

    elif i == " ":
        if not flag:
            if temp:
                result += temp[::-1]
                result.append(" ")
                temp = []
                continue

    if flag:
        result.append(i)
    else:
        temp.append(i)

if temp:
    result += temp[::-1]

print(*result, sep="")
