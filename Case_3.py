while True:

    x = int(input('x: '))

    if x == 12 or x<=2:
        print ('зима')
    elif x<=5 and x>2:
        print ('весна')
    elif x>5 and x<=8:
        print ('лето')
    elif x>8 and x<=11:
        print ('осень')
    else:
        print ('Error')
