N, L, W, H = map(int, input().split())

s, e = 0, min(L, W, H)

while s < e:
    m = (s + e) / 2

    if s == m or e == m:
        break

    if (L // m) * (W // m) * (H // m) >= N:
        s = m
    else:
        e = m

print(e)
