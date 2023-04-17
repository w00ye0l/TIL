n = int(input())

address = []

for _ in range(n):
    temp = list(map(int, input().split(".")))
    add = ""

    for i in range(4):
        add += bin(temp[i])[2:].zfill(8)

    address.append(add)

# 네트워크 마스크 계산을 위해 같은 idx(m)를 찾기
idx = 32

for i in range(31, -1, -1):
    flag = False
    for j in range(1, n):
        if address[j][i] != address[j - 1][i]:
            flag = True

    if flag:
        idx = i

# 네트워크 마스크 문자열로 생성
tempNetMask = "1" * idx + "0" * (32 - idx)
netMask = [255, 255, 255, 255]

# 네트워크 마스크 4개의 숫자로 분할 후 10진수로 변환
for i in range(0, 25, 8):
    netMask[i // 8] = netMask[i // 8] & int(tempNetMask[i : i + 8], 2)

# 네트워크 주소 구하기
netAddress = []

# 네트워크 마스크와 AND 비트 연산을 통해 계산
# 하나만 계산해도 다른 것과 같기 때문에 0번째로 계산
for i in range(4):
    netAddress.append(netMask[i] & int(address[0][i * 8 : i * 8 + 8], 2))

print(*netAddress, sep=".")
print(*netMask, sep=".")
