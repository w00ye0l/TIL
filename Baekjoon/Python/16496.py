n = int(input())

arr = list(map(str, input().split()))

arr.sort(key=lambda x: x * 9, reverse=True)

print(arr)

result = "".join(arr)

print(str(int(result)))
