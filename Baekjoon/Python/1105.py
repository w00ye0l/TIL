l, r = input().split()

cnt = 0

if len(l) != len(r):
    print(cnt)
else:
    idx = 0

    while idx < len(r):
        if l[idx] == r[idx]:
            if l[idx] == "8":
                cnt += 1
            idx += 1
        else:
            break

    print(cnt)
