t = int(input())

for i in range(1, t+1):
    n = input()
    re_n = n[::-1]

    result = 1 if n == re_n else 0

    print(f'#{i} {result}')
