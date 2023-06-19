N = int(input())
P = int(input())

nums = [P]

if N >= 5:
    if P - 500 < 0:
        nums.append(0)
    else:
        nums.append(P - 500)
if N >= 10:
    nums.append(int(P * 0.9))
if N >= 15:
    if P - 2000 < 0:
        nums.append(0)
    else:
        nums.append(P - 2000)
if N >= 20:
    nums.append(int(P * 0.75))

nums.sort()

print(nums[0])
