while True:
    arr = input()
    check = []
    result = True

    if arr == '.':
        break

    for i in arr:
        if i == '(' or i == '[':
            check.append(i)
        elif i == ')':
            if not len(check) or check[-1] == '[':
                result = False
                break
            elif check[-1] == '(':
                check.pop()
        elif i == ']':
            if not len(check) or check[-1] == '(':
                result = False
                break
            elif check[-1] == '[':
                check.pop()

    if not check and result:
        print('yes')
    else:
        print('no')
