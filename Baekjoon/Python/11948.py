science = []
society = []

for _ in range(4):
    science.append(int(input()))

for _ in range(2):
    society.append(int(input()))

print(sum(science) - min(science) + sum(society) - min(society))
