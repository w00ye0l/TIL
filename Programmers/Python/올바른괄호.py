def solution(s):
    answer = True
    stack = []

    for i in list(s):
        if i == "(":
            stack.append(i)
        else:
            if stack:
                if stack[-1] == "(":
                    stack.pop()
            else:
                answer = False
                break

    if stack:
        answer = False

    return answer


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
