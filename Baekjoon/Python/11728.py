n, m = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

result = sorted(arr_1 + arr_2)

print(' '.join(map(str, result)))
