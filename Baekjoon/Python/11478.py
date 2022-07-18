s = input()
result = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        s2 = s[i:j+1]
        result.add(s2)

print(len(result))
