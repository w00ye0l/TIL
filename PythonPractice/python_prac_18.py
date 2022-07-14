# 1) method 사용
word = input()
w_dict = {}

for i in word:
    if w_dict.get(i) == None:
        w_dict[i] = word.count(i)

for k, v in w_dict.items():
    print(k, v, sep=' ')


# 2)
word = input()
w_dict = {}

for char in word:
    if not char in w_dict:
        w_dict[char] = 1
    else:
        w_dict[char] = w_dict[char] + 1

for k, v in w_dict.items():
    print(k, v)


# 3) simple for문
word = input()
w_dict = {}

for i in word:
    w_dict[i] = 0

for i in word:
    w_dict[i] += 1

for k, v in w_dict.items():
    print(k, v)


# 4)
word = input()
result = {}

for char in word:
    result[char] = result.get(char, 0) + 1

for k, v in result.items():
    print(k, v)
