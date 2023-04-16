def check():
    global answer

    for i in range(6):
        for j in range(6):
            for k in range(6):
                if i == j or j == k or k == i:
                    continue

                visited = [0] * 6
                puzzle = [word[i], word[j], word[k]]

                visited[i], visited[j], visited[k] = 1, 1, 1

                for a in range(3):
                    temp = ""
                    for b in range(3):
                        temp += puzzle[b][a]

                    for c in range(6):
                        if temp == word[c] and visited[c] == 0:
                            visited[c] = 1
                            break

                if sum(visited) == 6:
                    answer = puzzle
                    return


word = [input() for _ in range(6)]

answer = []

check()

if answer:
    print(*answer, sep="\n")
else:
    print(0)
