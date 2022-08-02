t = int(input())

for _ in range(t):
    n = int(input())
    n_number = set(map(int, input().split()))

    m = int(input())
    m_number = list(map(int, input().split()))

    for i in m_number:
        if i in n_number:
            print(1)
        else:
            print(0)
