n, m = map(int, input().split())

if n == 0:
    print(0)
else:
    weight = list(map(int, input().split()))

    nowWeight = 0
    bag = 1

    for i in range(n):
        if nowWeight + weight[i] <= m:
            nowWeight += weight[i]
        else:
            bag += 1
            nowWeight = weight[i]

    print(bag)
