from collections import defaultdict

color_dic = defaultdict(list)

num_dic = defaultdict(int)

for _ in range(5):
    color, num = input().split()

    color_dic[color].append(int(num))
    num_dic[int(num)] += 1

# 색의 개수, 숫자의 개수
c_len = len(color_dic)
n_len = len(num_dic)

# 숫자의 종류
n_keys = list(num_dic.keys())
n_keys.sort()

# 숫자가 각각 가지는 개수
n_values = list(num_dic.values())

result = 0

# 색이 모두 같은 경우
if c_len == 1:
    # 숫자의 종류가 5개이면서
    if n_len == 5:
        # 숫자가 모두 연속적일 때 (1)
        if n_keys[-1] - n_keys[0] == 4:
            result = 900 + n_keys[-1]

        # 색이 모두 같지만 숫자가 연속적이지 않을 경우 (4)
        else:
            result += n_keys[-1] + 600

# 숫자의 종류가 2개이면서
elif n_len == 2:
    # 숫자가 4개, 1개로 나뉠 때 (2)
    if (list(num_dic.values())[0] == 4 and list(num_dic.values())[1] == 1) or (
        list(num_dic.values())[0] == 1 and list(num_dic.values())[1] == 4
    ):
        for k, v in num_dic.items():
            if v == 4:
                result = 800 + k

    # 숫자가 3개, 2개로 나뉠 때 (3)
    elif (list(num_dic.values())[0] == 3 and list(num_dic.values())[1] == 2) or (
        list(num_dic.values())[0] == 2 and list(num_dic.values())[1] == 3
    ):
        for k, v in num_dic.items():
            if v == 3:
                result += k * 10
            elif v == 2:
                result += k

        result += 700

# 숫자의 종류가 5개이고
elif n_len == 5:
    # 숫자가 모두 연속적일 때 (5)
    if n_keys[-1] - n_keys[0] == 4:
        result += n_keys[-1] + 500

    # 숫자가 연속적이지 않은 경우 (9)
    else:
        result += max(n_keys) + 100

# 5장 중 3장의 숫자가 같은 경우 (6)
elif 3 in n_values:
    for k, v in num_dic.items():
        if v == 3:
            result += k + 400

# 5장 중 2장의 숫자가 같은 수가 2개일 경우 (7)
elif n_values.count(2) == 2:
    temp = []
    for k, v in num_dic.items():
        if v == 2:
            temp.append(k)

    result += 300 + (max(temp) * 10) + min(temp)

# 5장 중 2장의 숫자가 같은 경우 (8)
elif 2 in n_values:
    for k, v in num_dic.items():
        if v == 2:
            result += k + 200

# 어떤 경우도 해당되지 않는 경우 (9)
else:
    print(1)
    result += max(n_values) + 100

print(result)
