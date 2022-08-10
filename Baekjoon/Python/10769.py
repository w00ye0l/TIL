s = input()

happy_cnt = s.count(':-)')
sad_cnt = s.count(':-(')

if happy_cnt == 0 and sad_cnt == 0:
    print('none')
elif happy_cnt == sad_cnt:
    print('unsure')
elif happy_cnt > sad_cnt:
    print('happy')
elif happy_cnt < sad_cnt:
    print('sad')
