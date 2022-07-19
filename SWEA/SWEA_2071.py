t = int(input())

for i in range(1, t+1):
    arr = list(map(int, input().split()))
    print(f'#{i} {round(sum(arr)/10)}')
