while True:
    suit = int(input('Lear: '))
    dignity = int(input('Dignity: '))

    if dignity == 6:
        D = 'шестерка'
    elif dignity == 7:
        D = 'семерка'
    elif dignity == 8:
        D = 'восьмерка'
    elif dignity == 9:
        D = 'девятка'
    elif dignity == 10:
        D = 'десятка'
    elif dignity == 11:
        D = 'валет'
    elif dignity == 12:
        D = 'дама'
    elif dignity == 13:
        D = 'король'
    elif dignity == 14:
        D = 'туз'
    else:
        print ('FF')

    if suit == 1:
        S = 'пики'
    elif suit == 2:
        S = 'треф'
    elif suit == 3:
        S = 'бубен'
    elif suit == 4:
        S = 'червей'
    else:
        print ('GG')

    print (D,S)
