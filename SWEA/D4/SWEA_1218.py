t = 10

open_ = ["(", "{", "[", "<"]
close_ = [")", "}", "]", ">"]

for i in range(t):
    n = int(input())

    stack_ = list(input())

    chk = []
    sign = True

    for j in range(n):
        cur = stack_.pop(0)

        if cur in open_:
            chk.append(cur)
        elif cur in close_:
            if open_.index(chk[-1]) == close_.index(cur):
                chk.pop()
            else:
                sign = False
                break

    if chk or sign == False:
        print(f"#{i + 1} 0")
    else:
        print(f"#{i + 1} 1")
