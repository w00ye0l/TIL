import sys


def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
k_arr = {}
v_arr = {}

for i in range(1, n+1):
    s = input()
    k_arr[s] = i
    v_arr[i] = s

for j in range(m):
    chk = input()

    if chk.isdigit():
        print(v_arr[int(chk)])
    else:
        print(k_arr[chk])
