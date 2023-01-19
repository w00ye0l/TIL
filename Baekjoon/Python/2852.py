n = int(input())

one_score, two_score = 0, 0
one_time, two_time = 0, 0
end_time = 48 * 60

win = 0

for _ in range(n):
    team, time = input().split()

    m, s = map(int, time.split(":"))

    if team == "1":
        one_score += 1
    elif team == "2":
        two_score += 1

    if one_score > two_score:
        if win == 0 or win == 2:
            one_time += end_time - (m * 60 + s)
        win = 1
    elif one_score < two_score:
        if win == 0 or win == 1:
            two_time += end_time - (m * 60 + s)
        win = 2
    else:
        win = 0
        if team == "1":
            two_time -= end_time - (m * 60 + s)
        elif team == "2":
            one_time -= end_time - (m * 60 + s)

print(str(one_time // 60).zfill(2), str(one_time % 60).zfill(2), sep=":")
print(str(two_time // 60).zfill(2), str(two_time % 60).zfill(2), sep=":")
