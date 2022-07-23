dic = {}
n = int(input())
for i in range(n):
    a, b = list(input().split())
    dic[a] = b

dic = sorted(dic.items(), reverse=True)     # 딕셔너리 역순으로 정렬하기

for i in dic:
    if i[1] == 'enter':
        print(i[0])
