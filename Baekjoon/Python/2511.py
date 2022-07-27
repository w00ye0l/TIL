a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score = 0
b_score = 0
sign = 0

for i in range(10):
    if a[i] > b[i]:
        a_score += 3
        sign = 1
    elif a[i] == b[i]:
        a_score += 1
        b_score += 1
    else:
        b_score += 3
        sign = 2

print(a_score, b_score)
if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
else:
    if sign == 1:
        print('A')
    elif sign == 2:
        print('B')
    else:
        print('D')
