def solution(input_string):
    answer = ''

    s = list(input_string)
    al = []
    temp = set()

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            if s[i] in al:
                temp.add(s[i])
            else:
                al.append(s[i])

    if s[-1] in al:
        temp.add(s[-1])

    if temp:
        answer = ''.join(sorted(temp))
    else:
        answer = 'N'

    return answer


print(solution("zbzbz"))
