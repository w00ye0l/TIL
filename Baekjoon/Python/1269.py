import sys


def input():
    return sys.stdin.readline().rstrip()


a, b = map(int, input().split())

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

print(len(set_a ^ set_b))
