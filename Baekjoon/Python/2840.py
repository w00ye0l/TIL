N, K = map(int, input().split())

wheel = ["?"] * N
idx = 0
answer = "?"

for _ in range(K):
    S, alpha = input().split()
    S = int(S)

    idx = (idx + S) % N

    if wheel[idx] != "?" and wheel[idx] != alpha:
        answer = "!"
    else:
        wheel[idx] = alpha

for i in range(ord("A"), ord("Z") + 1):
    if wheel.count(chr(i)) >= 2:
        answer = "!"

if answer == "!":
    print(answer)
else:
    answer = wheel[idx::-1] + wheel[-1:idx:-1]
    print("".join(answer))
