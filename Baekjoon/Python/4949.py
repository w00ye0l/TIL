while True:
    s = input()
    stack_ = []
    result = 'yes'

    if s == '.':
        break

    for i in s:
        if i == '(' or i == '[':
            stack_.append(i)
        elif i == ')':
            if len(stack_) == 0 or stack_[-1] == '[':
                result = 'no'
                break
            elif stack_[-1] == '(':
                stack_.pop()
        elif i == ']':
            if len(stack_) == 0 or stack_[-1] == '(':
                result = 'no'
                break
            elif stack_[-1] == '[':
                stack_.pop()

    if len(stack_):
        result = 'no'

    print(result)
