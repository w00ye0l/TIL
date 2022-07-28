n = int(input())
have_card = list(map(int, input().split()))

m = int(input())
check_card = list(map(int, input().split()))

count_dic = {}

for i in have_card:
    if i not in count_dic:
        count_dic[i] = 1
    else:
        count_dic[i] += 1

for i in check_card:
    print(count_dic.get(i, 0), end=' ')
