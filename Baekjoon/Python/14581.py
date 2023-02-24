arr = input()

fan = ":fan:"
result = []

for i in range(3):
    temp = ""
    for j in range(3):
        if i == 1 and j == 1:
            temp += ":" + arr + ":"
        else:
            temp += fan
    result.append(temp)

print(*result, sep="\n")
