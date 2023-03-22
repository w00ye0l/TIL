n = int(input())
pattern = input().split("*")
l = len(pattern[0]) + len(pattern[1])

for _ in range(n):
    arr = input()

    if len(arr) < l:
        print("NE")
    else:
        if (
            pattern[0] == arr[: len(pattern[0])]
            and pattern[1] == arr[-len(pattern[1]) :]
        ):
            print("DA")
        else:
            print("NE")
