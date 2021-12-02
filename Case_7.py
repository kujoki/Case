while True:
    x = int(input('Ed: '))
    m = float(input('Mass: '))

    if x == 1:
        print ('Mass (kg): ',m)
    elif x == 2:
        m = m*10**(-6)
        print ('Mass (mg to kg): ',m)
    elif x == 3:
        m = m*10**(-3)
        print('Mass (g to kg): ',m)
    elif x == 4:
        m = m*10**(3)
        print ('Mass (t to kg): ',m)
    elif x == 5:
        m = m*10**(2)
        print ('Mass (z to kg)',m)
    else:
        print ('Error')
    
