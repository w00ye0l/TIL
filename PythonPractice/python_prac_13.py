# 1) slicing
word = input()

print(word[::-1])

# 2) for문
word = input()
re_word = ''

for char in word:
    re_word = char + re_word

print(re_word)
