N, A, B = map(int, input().split())

if N <= B:
    if A < B:
        print("Bus")
    elif A > B:
        print("Subway")
    else:
        print("Anything")
else:
    print("Bus")
