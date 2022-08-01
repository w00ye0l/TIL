import sys
input = sys.stdin.readline

n = int(input())

marathon = {}

for i in range(n):
    name = input()
    if name not in marathon:
        marathon[name] = 1
    else:
        marathon[name] += 1

for i in range(n-1):
    p = input()
    marathon[p] -= 1

for k, v in marathon.items():
    if v != 0:
        print(k)
