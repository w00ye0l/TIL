A, a, B, b, P = map(int, input().split())

if P >= A + B:
    print("Yes")
else:
    if A > P or B > P:
        print("No")
    else:
        if A >= B:
            if a >= B:
                print("Yes")
            else:
                print("No")
        else:
            if b >= A:
                print("Yes")
            else:
                print("No")
