N = int(input())

print("int a;")
for i in range(N):
    if i == 0:
        print("int " + (i + 1) * "*" + "ptr = &a;")
    else:
        print(f"int {'*' * (i + 1)}ptr{i + 1} = &ptr{i if i > 1 else ''};")
