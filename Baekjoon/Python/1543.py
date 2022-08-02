origin = input()
find = input()
cnt = 0

while find in origin:
    origin = origin.replace(find, "@")

print(origin.count("@"))
