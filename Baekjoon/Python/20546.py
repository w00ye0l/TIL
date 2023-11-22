money = int(input())

arr = list(map(int, input().split()))

junhyunM, junhyunC = money, 0
sungminM, sungminC = money, 0
down, up = 0, 0

for i in range(14):
    if arr[i] <= junhyunM:
        buy = junhyunM // arr[i]
        junhyunC += buy
        junhyunM -= buy * arr[i]

    if i != 0:
        if arr[i] < arr[i - 1]:
            down += 1
            up = 0
        elif arr[i] > arr[i - 1]:
            up += 1
            down = 0

    if down >= 3:
        if arr[i] <= sungminM:
            buy = sungminM // arr[i]
            sungminC += buy
            sungminM -= buy * arr[i]
    elif up >= 3:
        sungminM += sungminC * arr[i]
        sungminC = 0

if junhyunC * arr[-1] + junhyunM > sungminC * arr[-1] + sungminM:
    print("BNP")
elif junhyunC * arr[-1] + junhyunM < sungminC * arr[-1] + sungminM:
    print("TIMING")
else:
    print("SAMESAME")
