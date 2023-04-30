def bt(idx):
    if idx == k:
        answer_list.append("".join(map(str, visited)))
        return

    for i in range(10):
        if i in visited:
            continue

        if arr[idx] == "<":
            if visited[idx] < i:
                visited.append(i)
                bt(idx + 1)
                visited.pop()
        elif arr[idx] == ">":
            if visited[idx] > i:
                visited.append(i)
                bt(idx + 1)
                visited.pop()


k = int(input())

arr = list(input().split())

visited = []
answer_list = []

for i in range(10):
    visited.append(i)
    bt(0)
    visited.pop()

answer_list.sort()

print(answer_list[-1])
print(answer_list[0])
