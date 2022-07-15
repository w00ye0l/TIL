with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    lines = text.split('\n')
    fruit = {}

    for line in lines:
        if not line in fruit:
            fruit[line] = 1
        else:
            fruit[line] += 1

    with open('03.txt', 'w', encoding='utf-8') as a:
        for k, v in fruit.items():
            a.write(f'{k} {v}\n')
