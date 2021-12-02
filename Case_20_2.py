while True:
    d = int(input())
    m = int(input())

    months = 0
    if m>1:
        months += 31
    if m>2:
        months += 28
    if m>3:
        months += 31
    if m>4:
        months += 30
    if m>5:
        months += 31
    if m>6:
        months += 30
    if m>7:
        months += 31
    if m>8:
        months += 31
    if m>9:
        months += 30
    if m>10:
        months += 31
    if m>11:
        months += 30
        
    x = d+months
    
    if 20<=x<=49:
        print('Водолей')
    elif 50<=x<=79:
        print('Рыбы')
    elif 80<=x<=109:
        print('Овен')
    elif 110<=x<=140:
        print('Телец')
    elif 141<=x<=172:
        print('Близнецы')
    elif 173<=x<=203:
        print('Рак')
    elif 204<=x<=234:
        print('Лев')
    elif 235<=x<=265:
        print('Дева')
    elif 266<=x<=295:
        print('Весы')
    elif 296<=x<=326:
        print('Скорпион')
    elif 327<=x<=355:
        print('Стрелец')
    else:
        print('Козерог')
