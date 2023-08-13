cnt, answer = 0, 0

for i in range(10):
    a, b = map(int, input().split())
    
    cnt += b
    cnt -= a

    answer = max(answer, cnt)

print(answer)