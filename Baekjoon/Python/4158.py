# import sys

# input = sys.stdin.readline

# while True:
#     n, m = map(int, input().split())

#     if n == 0 and m == 0:
#         break

#     sang = []
#     for _ in range(n):
#         sang.append(int(input()))

#     cnt = 0
#     for _ in range(m):
#         sun = int(input())
#         # 상근이의 list에서 처음과 끝의 index를 판단
#         start, end = 0, n - 1

#         # start가 end보다 커지면 종료
#         while start <= end:
#             mid = (start + end) // 2

#             # 상근이에게 선영이가 가지고 있는 CD가 있다면
#             if sang[mid] == sun:
#                 # 개수를 추가하고 break
#                 cnt += 1
#                 break
#             # 만약 상근이의 인덱스 mid 값이 선영이의 CD 값보다 크다면 탐색 구간을 앞으로
#             elif sang[mid] > sun:
#                 end = mid - 1
#             # 상근이의 인덱스 mid 값이 선영이의 CD 값보다 작다면 탐색 구간을 뒤로
#             else:
#                 start = mid + 1

#     print(cnt)

# import sys

# input = sys.stdin.readline

# while True:
#     n, m = map(int, input().split())

#     if n == 0 and m == 0:
#         break

#     sang = set()
#     for _ in range(n):
#         sang.add(int(input()))

#     cnt = 0
#     for _ in range(m):
#         sun = int(input())

#         if sun in sang:
#             cnt += 1

#     print(cnt)

import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    sang = []
    for _ in range(n):
        sang.append(int(input()))

    sun = []
    for _ in range(m):
        sun.append(int(input()))

    pointer1, pointer2 = 0, 0
    cnt = 0

    while pointer1 < n and pointer2 < m:
        if sang[pointer1] < sun[pointer2]:
            pointer1 += 1
        elif sang[pointer1] > sun[pointer2]:
            pointer2 += 1
        else:
            cnt += 1
            pointer1 += 1
            pointer2 += 1

    print(cnt)
