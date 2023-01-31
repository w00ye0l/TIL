arr = input()

result = ""

for a in arr:
    if a.isalpha():
        if a.isupper():
            result += chr((ord(a) - ord("A") + 13) % 26 + ord("A"))
        else:
            result += chr((ord(a) - ord("a") + 13) % 26 + ord("a"))
    else:
        result += a

print(result)
