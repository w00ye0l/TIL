a, b = list(input().split())

re_a = int(a[::-1])
re_b = int(b[::-1])

print(re_a if re_a > re_b else re_b)
