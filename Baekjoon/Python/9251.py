str1 = input()
str2 = input()

len1, len2 = len(str1), len(str2)

dp = [0] * len2

for i in range(len1):
    cnt = 0
    for j in range(len2):
        # 현재까지 공통부분 중 가장 긴 것 찾기
        # print(cnt, j, dp[j])
        if cnt < dp[j]:
            cnt = dp[j]
        # 공통부분이 더 있을 경우 최대 길이 늘리기
        elif str1[i] == str2[j]:
            dp[j] = cnt + 1
            # print(str1[i], str2[j], cnt)
            # print(dp)

print(max(dp))
