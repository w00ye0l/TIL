def solution(sizes):
    answer = 0

    max_w, max_h = 0, 0
    for s in sizes:
        [w, h] = s
        if w < h:
            w, h = h, w

        if max_w < w:
            max_w = w

        if max_h < h:
            max_h = h

    answer = max_w * max_h

    return answer


print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
