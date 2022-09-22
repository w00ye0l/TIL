from django.shortcuts import render
import random

# Create your views here.


def todayDinner(response):
    food = [
        '돈까스',
        '마라탕',
        '삼겹살',
        '치킨',
        '피자',
    ]

    img = [
        'https://w.namu.la/s/271fe016d343b02c2351de8c7afa515d849ded0442809eccae51c8809cb2d21ce50aeed68493011a1212047d1599de8223158de8153c3e5505d3b2e7307e708b42f8e4f24db0c838094a6edbb8356708729dfed2f092a8b8554275da863fc0367154072676a9a7c41101455d03e32bb5',
        'https://img1.daumcdn.net/thumb/R1280x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/4BYf/image/_pc0k6Jz3BHHLVwylaQYEPZdQd0.jfif',
        'https://src.hidoc.co.kr/image/lib/2021/8/27/1630049987719_0.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/2/20/Korean_fried_chicken_3_banban.jpg',
        'https://w.namu.la/s/8c2aebf04d4c6e0ae24ebf3b3789cb064f353da40f0a2916630ee33cc34742414ac8427b8765569e84d615a24cac7bc389ada2e5c60579541ea8b41be9b22db6d0ce58f59fd1ac01912436c928605cd86974e360258a66ac0374662e70b0ae73',
    ]

    random_numlist = [i for i in range(len(food))]

    random_num = random.choice(random_numlist)

    context = {
        'name': food[random_num],
        'img': img[random_num],
    }

    return render(response, 'todayDinner.html', context)


def lotto(response):
    lotto_list = []
    correct_num = [3, 11, 15, 29, 35, 44]
    bonus_num = 10

    for i in range(5):
        lotto = random.sample(range(1, 46), 6)
        cnt = 0
        result = 0

        for l in lotto:
            if l in correct_num:
                cnt += 1

        if cnt < 3:
            result = 0
        elif cnt == 3:
            result = 5
        elif cnt == 4:
            result = 4
        elif cnt == 5:
            if bonus_num not in lotto:
                result = 3
            else:
                result = 2
        elif cnt == 6:
            result = 1

        lotto_list.append([sorted(lotto), result])

    context = {
        'lottos': lotto_list,
    }

    return render(response, 'lotto.html', context)
