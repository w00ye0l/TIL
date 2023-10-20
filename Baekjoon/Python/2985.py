a, b, c = input().split()

sign = ["+", "-", "*", "/"]

for s in sign:
    if eval(a + s + b) == int(c):
        print(a + s + b + "=" + c)
        break
    elif int(a) == eval(b + s + c):
        print(a + "=" + b + s + c)
        break
