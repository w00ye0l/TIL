N = int(input())

powerOne = 0
powerThree = 0

for i in range(1, N + 1):
    powerOne += i
    powerThree += i**3

print(powerOne, powerOne**2, powerThree, sep="\n")
