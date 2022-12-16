from itertools import combinations

arr = list(input())

idx = [i for i in range(len(arr) - 1)]
idx_pick = list(combinations(idx, 2))


result = []

for pick in idx_pick:
    temp = arr
    # print(
    #     temp[0 : pick[0] + 1][::-1],
    #     temp[pick[0] + 1 : pick[1] + 1][::-1],
    #     temp[pick[1] + 1 : len(arr)][::-1],
    # )

    result.append(
        "".join(temp[0 : pick[0] + 1][::-1])
        + "".join(temp[pick[0] + 1 : pick[1] + 1][::-1])
        + "".join(temp[pick[1] + 1 : len(arr)][::-1])
    )

print(sorted(result)[0])
