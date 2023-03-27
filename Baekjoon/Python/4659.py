while True:
    pw = input()

    inVowel = False
    vCnt = 0
    cCnt = 0
    result = True

    if pw == "end":
        break

    for i in ["a", "e", "i", "o", "u"]:
        if i in pw:
            inVowel = True

    for i in pw:
        if i in ["a", "e", "i", "o", "u"]:
            cCnt = 0
            vCnt += 1

            if vCnt == 3:
                result = False
                break
        else:
            vCnt = 0
            cCnt += 1

            if cCnt == 3:
                result = False
                break

    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1] and not pw[i : i + 2] in ["ee", "oo"]:
            result = False
            break

    if inVowel and result:
        print(f"<{pw}> is acceptable.")
    else:
        print(f"<{pw}> is not acceptable.")
