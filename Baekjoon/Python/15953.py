f_prize = [5000000, 3000000, 2000000, 500000, 300000, 100000]
s_prize = [5120000, 2560000, 1280000, 640000, 320000]
f_result = [0]
s_result = [0]

for i in range(len(f_prize)):
    f_result += [f_prize[i] for _ in range(i + 1)]

for i in range(len(s_prize)):
    s_result += [s_prize[i] for _ in range(2 ** i)]

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    result = 0

    if a >= len(f_result):
        a = 0
    if b >= len(s_result):
        b = 0

    result = f_result[a] + s_result[b]

    print(result)
