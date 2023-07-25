T = int(input())

for _ in range(T):
    arr = input()
    l_list, r_list = [], []

    for i in arr:
        if i == "<":
            if l_list:
                r_list.append(l_list.pop())
        elif i == ">":
            if r_list:
                l_list.append(r_list.pop())
        elif i == "-":
            if l_list:
                l_list.pop()
        else:
            l_list.append(i)

    print("".join(l_list + list(reversed(r_list))))
