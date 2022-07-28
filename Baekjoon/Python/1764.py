n, m = map(int, input().split())
not_hear = []
not_see = []
temp = []
result = []

for _ in range(n):
    s = input()
    not_hear.append(s)

for _ in range(m):
    s = input()
    not_see.append(s)

temp = not_hear + not_see
temp.sort()

for i in range(1, n + m):
    if temp[i] == temp[i - 1]:
        result.append(temp[i])

print(len(result))
for i in result:
    print(i)


# n,m=map(int,input().split())
# n_list=set()
# m_list=set()
# nm_list=[]
# cnt=0

# for i in range(n):
#     name=input()
#     n_list.add(name)

# for i in range(m):
#     name=input()
#     m_list.add(name)

# nm_list=sorted((n_list&m_list))
# print(len(nm_list))
# for i in range(len(nm_list)):
#     print(nm_list[i])
