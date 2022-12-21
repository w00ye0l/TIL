exp = input()

stack_ = []
result = ""

for e in exp:
    if e.isalpha():
        result += e
    else:
        if e == "(":
            stack_.append(e)
        elif e == ")":
            while stack_ and stack_[-1] != "(":
                result += stack_.pop()
            stack_.pop()
        elif e == "*" or e == "/":
            while stack_ and (stack_[-1] == "*" or stack_[-1] == "/"):
                result += stack_.pop()
            stack_.append(e)
        elif e == "+" or e == "-":
            while stack_ and stack_[-1] != "(":
                result += stack_.pop()
            stack_.append(e)
    print(result, stack_)

while stack_:
    result += stack_.pop()

print(result)
