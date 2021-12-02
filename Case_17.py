while True:
    num = int(input('Enter count: '))

    if num//10 == 1:
        if num == 10:
            print ('десять учебных заданий')
        elif num == 11:
            print ('одинадцать учебных заданий')
        elif num == 12:
            print ('двенадцать учебных заданий')
        elif num == 13:
            print ('тринадцать учебных заданий')
        elif num == 14:
            print ('четырнадцать учебных заданий')
        elif num == 15:
            print ('пятнадцать учебных заданий')
        elif num == 16:
            print ('шестнадцать учебных заданий')
        elif num == 17:
            print ('семнадцать учебных заданий')
        elif num == 18:
            print ('восемнадцать учебных заданий')
        elif num == 19:
            print ('девятнадцать учебных заданий')
    else:
         None

    if num//10 == 2:
        n_1 = 'двадцать'
    elif num//10 == 3:
        n_1 = 'тридцать'
    elif num//10 == 4:
        n_1 = 'сорок'
    '''else:
        print ('Error_1')'''

    if num%10 == 0:
        n_2 = ' '
    elif num%10 == 1:
        n_2 = 'одно'
    elif num%10 == 2:
        n_2 = 'два'
    elif num%10 == 3:
        n_2 = 'три'
    elif num%10 == 4:
        n_2 = 'четыре'
    elif num%10 == 5:
        n_2 = 'пять'
    elif num%10 == 6:
        n_2 = 'шесть'
    elif num%10 == 7:
        n_2 = 'семь'
    elif num%10 == 8:
        n_2 = 'восемь'
    elif num%10 == 9:
        n_2 = 'девять'
    '''else:
        print ('Error_2')'''

    if num%10 == 0 or num%10 == 5 or num%10 == 6 or num%10 == 7 or num%10 == 8 or num%10 == 9:
        n_3 = 'учебных заданий'
    elif num%10 == 1:
        n_3 = 'учебное задание'
    elif num%10 == 2 or num%10 == 3 or num%10 == 4:
        n_3 = 'учебных задания'
    '''else:
        print ('Error_3')'''
        
    if num >= 20:
        print (n_1, n_2, n_3)
