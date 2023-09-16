N = int(input())
chrGubun = list(input().split())
M = int(input())
numGubun = list(input().split())
K = int(input())
byeonghab = list(input().split())
S = int(input())
arr = input()

answer = []
stack_ = []

for i in range(S):
    if arr[i] in chrGubun or arr[i] in numGubun or arr[i] == " ":
        if arr[i] in byeonghab:
            stack_.append(arr[i])
        else:
            if stack_:
                answer.append("".join(stack_))
                stack_ = []
    else:
        stack_.append(arr[i])

if stack_:
    answer.append("".join(stack_))

print(*answer, sep="\n")
