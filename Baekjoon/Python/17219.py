n, m = map(int, input().split())

dic = {}
for _ in range(n):
    url, pw = input().split()

    dic[url] = pw

for _ in range(m):
    print(dic[input()])
