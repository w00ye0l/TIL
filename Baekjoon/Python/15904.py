s = input()

result = ""

for i in s:
    if i == 'U' and result == "":
        result += i
    elif i == 'C' and result == "U":
        result += i
    elif i == 'P' and result == "UC":
        result += i
    elif i == 'C' and result == "UCP":
        result += i

if result != "UCPC":
    print('I hate UCPC')
else:
    print('I love UCPC')
