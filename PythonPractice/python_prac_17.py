# 1) 문자열을 리스트화한 뒤 다시 문자열로
word = list(input())

for i in range(len(word)):
    chk = ord(word[i])
    if chk >= ord('a'):
        chk -= ord('a') - ord('A')
        word[i] = chr(chk)

word = ''.join(word)
print(word)


# 2) 새로운 문자열에 추가
word = input()
re_word = ''

for i in range(len(word)):
    chk = ord(word[i])
    if chk >= ord('a'):
        chk -= ord('a') - ord('A')
        re_word += chr(chk)

print(re_word)
