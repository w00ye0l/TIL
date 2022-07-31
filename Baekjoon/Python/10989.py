import sys
input = sys.stdin.readline

n = int(input())

dic = {}
max_ = 0

for i in range(n):
    number = int(input())
    if max_ < number:
        max_ = number
    if str(number) not in dic:
        dic[str(number)] = 1
    else:
        dic[str(number)] += 1

for i in range(1, max_ + 1):
    if dic.get(str(i)) != None:
        for j in range(dic[str(i)]):
            print(i)

##############

# import sys
# input = sys.stdin.readline

# n = int(input())

# numbers = [0] * 10001

# for i in range(n):
#     number = int(input())
#     numbers[number] += 1

# for i in range(10001):
#     if numbers[i] != 0:
#         for j in range(numbers[i]):
#             print(i)
