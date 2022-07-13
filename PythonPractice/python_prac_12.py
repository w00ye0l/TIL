# 1) replace() 함수 사용
word = input()

print(word.replace('a', ''))

# 2) for문
word = list(input())

for x in range(len(word)):
    if word[x] == 'a':
        word[x] = ''
re_word = ''.join(word)

print(re_word)
