arr = input()

result = ""
for a in arr:
    if a.isupper():
        result += a.lower()
    else:
        result += a.upper()

print(result)
