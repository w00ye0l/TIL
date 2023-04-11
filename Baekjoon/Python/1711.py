import sys

input = sys.stdin.readline

n = int(input())

node = []
result = 0

for _ in range(n):
    node.append(tuple(map(int, input().split())))

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            n1, n2, n3 = node[i], node[j], node[k]
            a = (n1[0] - n2[0]) ** 2 + (n1[1] - n2[1]) ** 2
            b = (n2[0] - n3[0]) ** 2 + (n2[1] - n3[1]) ** 2
            c = (n3[0] - n1[0]) ** 2 + (n3[1] - n1[1]) ** 2

            if 2 * max(a, b, c) == a + b + c:
                result += 1

print(result)
