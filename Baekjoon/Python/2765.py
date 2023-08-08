T = 1

while True:
    d, cnt, t = map(float, input().split())

    if cnt == 0:
        break

    dis = d * 3.1415927 * cnt / 12 / 5280
    speed = dis / (t / 3600)

    print(f"Trip #{T}: {dis:.2f} {speed:.2f}")

    T += 1
