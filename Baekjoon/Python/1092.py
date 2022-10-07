n = int(input())

crane = list(map(int, input().split()))
crane.sort(reverse=True)

m = int(input())

box = list(map(int, input().split()))
box.sort(reverse=True)

t = 0

if crane[0] < box[0]:
    print(-1)
else:
    while box:
        for c in crane:
            if not box:
                break

            elif c < box[-1]:
                break

            else:
                for b in box:
                    if c >= b:
                        box.remove(b)
                        break

        t += 1

    print(t)
