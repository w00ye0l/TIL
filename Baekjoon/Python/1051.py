n, m = map(int, input().split())
arr = []
area = []

for i in range(n):
    s = list(input())
    arr.append(s)

for i in range(n):                          # 행 이동
    for j in range(m):                      # 열 이동
        for k in range(min(n, m)):          # 정사각형 길이
            # (행 + 정사각형 길이)가 최대 행의 길이보다 작아야 함, (열 + 정사각형 길이)가 최대 열의 길이보다 작아야 함
            if (i + k) < n and (j + k) < m:
                if arr[i][j] == arr[i][j + k] == arr[i + k][j] == arr[i + k][j + k]:
                    area.append((k + 1)**2)

print(max(area))
