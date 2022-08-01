names = list(input().split('-'))

result = ""

for i in range(len(names)):
    result += names[i][0]

print(result)
