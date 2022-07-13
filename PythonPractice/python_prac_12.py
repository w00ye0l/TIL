# 1) replace() 함수 사용
word = input()

print(word.replace('a', ''))


# 2) for문
word = input()
re_word = ''

for x in word:
    if x == 'a':
        continue
    re_word += x

print(re_word)


# 3) for문
word = list(input())

for x in range(len(word)):
    if word[x] == 'a':
        word[x] = ''
re_word = ''.join(word)

print(re_word)
