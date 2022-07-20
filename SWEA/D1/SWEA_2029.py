t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'#{i} {a//b} {a%b}')
