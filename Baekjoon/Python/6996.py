n = int(input())

for _ in range(n):
    s = list(input().split())
    temp = []

    for i in s:
        temp.append(sorted(list(i)))

    if temp[0] == temp[1]:
        print(f'{"".join(s[0])} & {"".join(s[1])} are anagrams.')
    else:
        print(f'{"".join(s[0])} & {"".join(s[1])} are NOT anagrams.')
