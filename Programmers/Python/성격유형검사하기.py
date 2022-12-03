def solution(survey, choices):
    answer = ""

    dic = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }

    for i in range(len(survey)):
        score = abs(4 - choices[i])
        if choices[i] < 4:
            dic[survey[i][0]] += score
        else:
            dic[survey[i][1]] += score

    if dic["R"] < dic["T"]:
        answer += "T"
    else:
        answer += "R"

    if dic["C"] < dic["F"]:
        answer += "F"
    else:
        answer += "C"

    if dic["J"] < dic["M"]:
        answer += "M"
    else:
        answer += "J"

    if dic["A"] < dic["N"]:
        answer += "N"
    else:
        answer += "A"

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))
