while True:

    x = int(input('x: '))

    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
        print ('Число дней: 31')
    elif x == 2:
        print ('Число дней: 28')
    elif x == 4 or x == 6 or x == 9 or x == 11:
        print ('Число дней: 30')
    else:
        print ('Error')
