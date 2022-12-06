dic = {
    "0": 4,
    "1": 2,
}

while True:
    arr = input()

    if arr == "0":
        break

    result = 1
    for i in arr:
        if i in dic:
            result += dic[i]
        else:
            result += 3
        result += 1

    print(result)
