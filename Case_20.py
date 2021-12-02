while True:
    d = int(input('Enter day: '))
    m = int(input('Enter month: '))

    if (d>=20 and m == 1) or (m == 2 and d <=18 ):
        print ('Водолей')
    elif (d>=19 and m == 2) or (d<=20 and m == 3):
        print ('Рыбы')
    elif (d >= 21 and m == 3) or (d<=19 and m == 4):
        print ('Овен')
    elif (d>=20 and m == 4) or (d<=20 and m == 5):
        print ('Телец')
    elif (d>=21 and m == 5) or (d<= 21 and m == 6):
        print ('Близнецы')
    elif (d>=22 and m == 6) or (d<= 22 and m == 7):
        print ('Рак')
    elif (d>=23 and m == 7) or (d<= 22 and m == 8):
        print ('Лев')
    elif (d>= 23 and m == 8) or (d<= 22 and m == 9):
        print ('Дева')
    elif (d>= 23 and m == 9) or (d<= 22 and m == 10):
        print ('Весы')
    elif (d>= 23 and m == 10) or (d<= 22 and m == 11):
        print ('Скорпион')
    elif (d>= 23 and m == 11) or (d<= 21 and m == 12):
        print ('Стрелец')
    elif (d>= 22 and m == 12) or (d<= 19 and m == 1):
        print ('Козерог')
    else:
        print ('ph')
