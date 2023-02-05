while True:
    arr = input()

    if arr == "END":
        break

    arr = list(arr)
    arr.reverse()

    print("".join(arr))
