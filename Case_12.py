while True:
    Num = int(input('Load: '))
    meaning = float(input('Meaninig: '))

    if Num == 1:
        R = meaning
        D = 2*R
        L = 3.14*2*R
        S = 3.14*R**2
        print ('R =',R,'D =',D,'L =',L,'S =',S)
    elif Num == 2:
        D = meaning
        R = D/2
        L = 3.14*2*R
        S = 3.14*R**2
        print ('R =',R,'D =',D,'L =',L,'S =',S)
    elif Num == 3:
        L = meaning
        R = L/(3.14*2)
        D = 2*R
        S = 3.14*R**2
        print ('R =',R,'D =',D,'L =',L,'S =',S)
    elif Num == 4:
        S = meaning
        R = (S/3.14)**(0.5)
        D = 2*R
        L = 3.14*2*R
        print ('R =',R,'D =',D,'L =',L,'S =',S)
    else:
        print ('Error')
        
    
    
