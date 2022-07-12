numbers = [0, 20, 100]
f = numbers[0]
s = numbers[1]

if f < s:
    f, s = s, f

for x in numbers:
    if x > f:
        s = f
        f = x
    elif x == f:
        continue
    else:
        if x >= s:
            s = x
print(s)
