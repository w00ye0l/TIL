def undo(target):
    for i in range(len(result) - 1, -1, -1):
        if target > result[i][0]:
            return result[i][1]
    else:
        return ""


n = int(input())

result = []
arr = ""

for i in range(n):
    order, text, time = input().split()

    if order == "type":
        arr += text
        result.append((int(time), arr))
    else:
        text, time = int(text), int(time)
        arr = undo(time - text)
        result.append((time, arr))

print(result[-1][1])
