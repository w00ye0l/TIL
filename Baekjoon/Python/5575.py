for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())

    et = eh * 3600 + em * 60 + es
    st = sh * 3600 + sm * 60 + ss

    rt = et - st

    rh = rt // 3600
    rm = (rt % 3600) // 60
    rs = (rt % 3600) % 60

    print(rh, rm, rs)
