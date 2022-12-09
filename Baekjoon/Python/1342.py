from collections import Counter


def backTracking(pre, cnt):
    answer = 0

    if cnt == len(arr):
        return 1

    for i in alpha.keys():
        if i == pre or alpha[i] == 0:
            continue

        alpha[i] -= 1
        answer += backTracking(i, cnt + 1)
        alpha[i] += 1

    return answer


arr = list(input())
alpha = Counter(arr)
print(backTracking("", 0))


# def dfs(idx, cur):
#     global result

#     if idx == len(arr):
#         result += 1
#         return

#     for i in range(26):
#         if alpha[i] == 0:
#             continue

#         if cur != "" and cur[-1] == chr(i + ord("a")):
#             continue

#         alpha[i] -= 1
#         dfs(idx + 1, cur + chr(i + ord("a")))
#         alpha[i] += 1


# arr = list(input())
# alpha = [0] * 26
# result = 0

# for i in range(len(arr)):
#     alpha[ord(arr[i]) - ord("a")] += 1

# dfs(0, "")

# print(result)
