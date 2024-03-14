N = int(input())

result = 1

for i in range(1, N + 1):
    result = result * i

result = str(result)[::-1]

for r in result:
    if r != "0":
        print(r)
        break
