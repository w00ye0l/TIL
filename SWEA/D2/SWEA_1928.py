t = int(input())
dic = {}

for i in range(ord('A'), ord('Z')+1):
    dic[chr(i)] = i - ord('A')
for i in range(ord('a'), ord('z')+1):
    dic[chr(i)] = i - ord('a') + 26
for i in range(ord('0'), ord('9')+1):
    dic[chr(i)] = i - ord('0') + 52
dic.update({'+': 62, '/': 63})

for i in range(1, t + 1):
    arr = input()
    re = ""
    for a in arr:
        re += f'{dic[a]:06b}'

    result = ""
    for j in range(0, len(re), 8):
        result += chr(int(re[j:j + 8], 2))

    print(f'#{i} {result}')
