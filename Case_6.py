while True:
    x = int(input('Ed: '))
    l = float(input('Lengh: '))

    if x == 1:
        m = l*0,1
        print ('Lengh (dm to m): ',m)
    elif x == 2:
        m = l*1000
        print ('Lengh (km to m): ',m)
    elif x == 3:
        m = l*10**(-3)
        print('Lengh (mm to m): ',m)
    elif x == 4:
        m = l*10**(-2)
        print ('Lengh (cm to m): ',m)
    else:
        print ('Error')
    
                                                                                    
