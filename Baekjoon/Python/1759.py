from itertools import combinations

vowel = {"a", "e", "i", "o", "u"}


l, c = map(int, input().split())

arr = list(input().split())

result = []
for com in set(combinations(arr, l)):
    if len(set(com) & vowel) >= 1 and len(com) - len(set(com) & vowel) >= 2:
        result.append("".join(sorted(list(com))))

print(*sorted(result), sep="\n")
