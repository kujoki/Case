while True:

    x = int(input('x: '))

    A = int(input('A: '))
    B = int(input('B: '))

    if x == 1:
        print (A+B)
    elif x == 2:
        print (A-B)
    elif x == 3:
        print (A*B)
    elif x == 4:
        print (A/B)
    else:
        print ('Error')
