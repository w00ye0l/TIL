def check():
    for m in mobis:
        if m not in arr:
            return False

    return True


arr = input()
mobis = ["M", "O", "B", "I", "S"]

if check():
    print("YES")
else:
    print("NO")
