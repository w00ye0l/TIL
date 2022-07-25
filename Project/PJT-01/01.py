with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    cnt = 0

    text = f.read()
    lines = text.split('\n')

    for line in lines:
        cnt += 1

    with open('01.txt', 'w', encoding='utf-8') as a:
        a.write(f'{cnt}')
