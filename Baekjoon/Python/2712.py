T = int(input())

for _ in range(T):
    num, unit = input().split()

    num = float(num)

    if unit == "kg":
        print(f"{num * 2.2046:.4f} lb")
    elif unit == "lb":
        print(f"{num * 0.4536:.4f} kg")
    elif unit == "l":
        print(f"{num * 0.2642:.4f} g")
    elif unit == "g":
        print(f"{num * 3.7854:.4f} l")
