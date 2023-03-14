n = int(input())
node = []
result = 0

for i in range(n):
    node.append(tuple(map(int, input().split())))

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            area = (1 / 2) * abs(
                node[i][0] * node[j][1]
                + node[j][0] * node[k][1]
                + node[k][0] * node[i][1]
                - (
                    node[i][1] * node[j][0]
                    + node[j][1] * node[k][0]
                    + node[k][1] * node[i][0]
                )
            )

            result = max(result, area)

print(result)
