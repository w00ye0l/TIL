s = list(input())
check = []
x_cnt = 0
result = ""

for i in s:
    if i == 'X':
        check.append(1)
    else:
        check.append(0)

for i in range(len(check)):
    if check[i] == 1:
        x_cnt += 1
    elif check[i] == 0:
        if x_cnt % 2 == 0:
            result += 'AAAA' * (x_cnt // 4)
            result += 'B' * (x_cnt % 4)
            x_cnt = 0
            result += '.'
        else:
            result = '-1'
            break

    if i == (len(check) - 1):
        if x_cnt % 2 == 0:
            result += 'AAAA' * (x_cnt // 4)
            result += 'B' * (x_cnt % 4)
        else:
            result = '-1'
            break

print(result)
