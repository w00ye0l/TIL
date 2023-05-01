n = int(input())

arr = list(map(int, input().split()))

if n == 1:
    print("A")
elif n == 2:
    if arr[0] != arr[1]:
        print("A")

    elif arr[0] == arr[1]:
        print(arr[0])
else:
    flag = False
    ta = arr[0] - arr[1]
    tb = arr[1] - arr[2]

    if ta == 0 and tb != 0:
        print("B")
    else:
        if ta == 0 and tb == 0:
            a = 1
            b = 0
        else:
            a = tb // ta
            b = arr[1] - arr[0] * a

            if tb % ta != 0:
                flag = True

        for i in range(1, n - 1):
            if arr[i] * a + b != arr[i + 1]:
                flag = True

        if flag:
            print("B")
        else:
            print(arr[-1] * a + b)
