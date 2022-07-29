data = []

n = int(input())

for i in range(n):
    data.append(list(input().split()))

data = sorted(data, key=lambda x: (int(x[3]), int(x[2]), int(x[1])))

print(data[-1][0], data[0][0], sep='\n')
