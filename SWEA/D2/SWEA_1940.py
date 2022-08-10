t = int(input())

for tt in range(1, t + 1):
    n = int(input())

    dis = 0
    speed = 0

    for i in range(n):
        s = list(input().split())
        if s[0] == '1':
            speed += int(s[1])
        elif s[0] == '2':
            if int(s[1]) > speed:
                speed = 0
            else:
                speed -= int(s[1])

        dis += speed * 1

    print(f'#{tt} {dis}')
