# arr = input()
# bomb = input()

# while True:
#     if bomb in arr:
#         arr = arr.replace(bomb, "")
#     else:
#         break

# if arr:
#     print(arr)
# else:
#     print("FRULA")

arr = input()
bomb = input()
l = len(bomb)

result = []

for a in arr:
    result.append(a)
    if "".join(result[-l:]) == bomb:
        for _ in range(l):
            result.pop()

if result:
    print("".join(result))
else:
    print("FRULA")
