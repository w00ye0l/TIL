mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    s = input()
    if s == '#':
        break

    result = 0
    for m in mo:
        result += s.count(m)

    print(result)
