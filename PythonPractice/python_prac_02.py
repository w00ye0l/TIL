# 1) for문
word = 'happy!'
n = 0
for idx in word:
    n += 1
print(n)

# 2) while문
word = 'happy!'
n = 0
while(word != ""):
    n += 1
    word = word[1:]
print(n)

# 3) while문
word = 'happy!'
n = 0
while(bool(word[n:]) == True):
    n += 1
print(n)
