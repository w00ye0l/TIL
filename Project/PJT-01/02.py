with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    lines = text.split('\n')
    cnt = 0
    berry = []

    for line in lines:
        if line.endswith('berry'):
            if not line in berry:
                berry.append(line)
                cnt += 1

    with open('02.txt', 'w', encoding='utf-8') as a:
        a.write(f'{cnt}\n')

        for line in berry:
            a.write(f'{line}\n')
