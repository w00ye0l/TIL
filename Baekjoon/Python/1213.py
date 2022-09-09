arr = list(input())

alphabet = [0] * 26

for i in arr:
    alphabet[ord(i) - ord('A')] += 1

result = ''
odd = 0
for i in range(26):
    if alphabet[i] % 2 != 0:
        odd += 1
        result = chr(i + ord('A'))

if (len(arr) % 2 == 0 and odd != 0) or (len(arr) % 2 != 0 and odd != 1):
    print("I'm Sorry Hansoo")
else:
    while len(result) != len(arr):
        for i in range(25, -1, -1):
            if alphabet[i] >= 2:
                alphabet[i] -= 2
                add_a = i + ord('A')
                result = chr(add_a) + result + chr(add_a)
                break

    print(result)
