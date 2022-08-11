for i in range(3):
    nums = input()
    cnt = 1
    cnt_list = []

    for j in range(7):
        if nums[j] == nums[j + 1]:
            cnt += 1
        else:
            cnt_list.append(cnt)
            cnt = 1

        cnt_list.append(cnt)

    print(max(cnt_list))
