import sys

s = sys.stdin.read()
alphabet = [0] * 26

for a in s:
    if a.islower():
        alphabet[ord(a) - ord('a')] += 1

for i in range(26):
    if alphabet[i] == max(alphabet):
        print(chr(i + ord('a')), end='')
