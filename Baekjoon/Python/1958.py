words = []

for _ in range(3):
    words.append(" " + input())


def lcs(one, two, three):
    dp = [
        [[0 for _ in range(len(three))] for _ in range(len(two))]
        for _ in range(len(one))
    ]

    for i in range(len(one)):
        for j in range(len(two)):
            for k in range(len(three)):
                if i == 0 or j == 0 or k == 0:
                    dp[i][j][k] = 0
                elif one[i] == two[j] and two[j] == three[k]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[len(one) - 1][len(two) - 1][len(three) - 1]


print(lcs(words[0], words[1], words[2]))
