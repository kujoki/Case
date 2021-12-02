while True:
    c = str(input('C: '))
    num = int(input('Num: '))

    if c == 'Ю':
        c = 0
    elif c == 'З':
        c = 1
    elif c == 'С':
        c = 2
    elif c == 'В':
        c = 3
    c = (c+num)%4
    if c==0:
        print('Ю')
    elif c==1:
        print('З')
    elif c==2:
        print('С')
    elif c==3:
        print('В')
'''
    if c == 'Ю' and num == 0:
        print ('Направление: ',c)
    elif c == 'З' and num == 0:
        print ('Направление: ',c)
    elif c == 'С' and num == 0:
        print ('Направление: ',с)
    elif c == 'В' and num == 0:
        print ('Направление: ',с)
    elif c == 'Ю' and num == -1:
        c = 'В'
        print ('Направление: ',c)
    elif c == 'З' and num == -1:
        c = 'Ю'
        print ('Направление: ',c)
    elif c == 'С' and num == -1:
        c = 'З'
        print ('Направление: ',с)
    elif c == 'В' and num == -1:
        c = 'С'
        print ('Направление: ',с)
    elif c == 'Ю' and num == 1:
        c = 'З'
        print ('Направление: ',c)
    elif c == 'З' and num == 1:
        c = 'С'
        print ('Направление: ',c)
    elif c == 'С' and num == 1:
        c = 'В'
        print ('Направление: ',с)
    elif c == 'В' and num == 1:
        c = 'Ю'
        print ('Направление: ',с)
'''
