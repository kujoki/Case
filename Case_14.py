while True:
    num = int(input('Enter num: '))
    meaning = float(input('Enter meaning: '))

    if num == 1:
        a = meaning
        R_1 = (a*(3)**0.5)/6
        R_2 = 2*R_1
        S = (a**2*3**0.5)/4
        print ('a:',a,'R_1:',R_1,'R_2:',R_2,'S:',S)
    elif num == 2:
        R_1 = meaning
        R_2 = R_1*2
        a = R_1*6/3**0.5
        S = (a**2*3**0.5)/4
        print ('a:',a,'R_1:',R_1,'R_2:',R_2,'S:',S)
    elif num == 3:
        R_2 = meaning
        R_1 = R_2/2
        a = R_1*6/3**0.5
        S = (a**2*3**0.5)/4
        print ('a:',a,'R_1:',R_1,'R_2:',R_2,'S:',S)
    elif num == 4:
        S = meaning
        a = (4*S/3**0.5)**0.5
        R_1 = (a*(3)**0.5)/6
        R_2 = 2*R_1
        print ('a:',a,'R_1:',R_1,'R_2:',R_2,'S:',S)
