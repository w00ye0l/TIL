def solution(brown, yellow):
    answer = []

    y_c, y_r = 0, 0
    b_c, b_r = 0, 0

    for i in range(yellow, 0, -1):
        y_c = i

        if yellow % y_c == 0:
            y_r = yellow // y_c
        else:
            continue

        b_c = y_c + 2
        b_r = y_r + 2

        if (b_r * 2) + (b_c * 2) - 4 == brown:
            break

    answer.append(b_c)
    answer.append(b_r)

    return answer


print(solution(8, 1))
