t = int(input())

for i in range(1, t + 1):
    num = list(map(int, input().split()))
    num.sort()
    num = num[1:9]

    print(f'#{i} {round(sum(num) / 8)}')
