def rectangle():
    a, b = map(int, input().split())
    return (a * b), ((a + b) * 2)


print(rectangle())
