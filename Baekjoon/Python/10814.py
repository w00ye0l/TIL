n = int(input())
inform_dic = dict()

for _ in range(n):
    k, v = input().split()

    k = int(k)

    if k in inform_dic:
        inform_dic[k] += [v]
    else:
        inform_dic[k] = [v]

for k in sorted(inform_dic):
    for v in inform_dic[k]:
        print(f'{k} {v}')
