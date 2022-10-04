a, b = input().split()

cnt = 1

while True:
    if b == a:
        break
    elif int(b) < int(a) or b == "":
        cnt = -1
        break

    if b[-1] == "1":
        b = b[:-1]
    elif int(b) % 2 == 0:
        b = str(int(b) // 2)
    else:
        if b != a:
            cnt = -1
            break

    cnt += 1

print(cnt)
