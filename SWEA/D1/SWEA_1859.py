t = int(input())

for i in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    buy = [0 for i in range(n)]
    sell = [0 for i in range(n)]
    for j in range(n):
        buy[j+1] += arr[j]
        sell[j+1] += 1*arr[j]

    print(buy)
    print(sell)
