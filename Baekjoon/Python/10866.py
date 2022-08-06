from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deque_ = deque()

for _ in range(n):
    s = list(input().split())

    if s[0] == 'push_front':
        deque_.appendleft(s[1])
    elif s[0] == 'push_back':
        deque_.append(s[1])
    elif s[0] == 'pop_front':
        if len(deque_) == 0:
            print('-1')
        else:
            print(deque_.popleft())
    elif s[0] == 'pop_back':
        if len(deque_) == 0:
            print('-1')
        else:
            print(deque_.pop())
    elif s[0] == 'size':
        print(len(deque_))
    elif s[0] == 'empty':
        if len(deque_):
            print('0')
        else:
            print('1')
    elif s[0] == 'front':
        if len(deque_) == 0:
            print('-1')
        else:
            print(deque_[0])
    elif s[0] == 'back':
        if len(deque_) == 0:
            print('-1')
        else:
            print(deque_[-1])
