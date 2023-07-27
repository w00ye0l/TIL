a, b = input().split()

list_a = list(a)
b = int(b)

idx = a.index(".")
d_idx = len(a) - 1 - idx
final_idx = d_idx * b

list_a.remove(".")
temp_a = int("".join(list_a))
temp_result = temp_a**b
list_result = list(str(temp_result))

answer = []
while True:
    if list_result:
        answer.append(list_result.pop())
    else:
        answer.append("0")

    if final_idx > 0:
        final_idx -= 1
        if final_idx == 0:
            answer.append(".")

    if not (list_result or final_idx):
        if answer[-1] == ".":
            answer.append("0")

        break

print(*list(reversed(answer)), sep="")
