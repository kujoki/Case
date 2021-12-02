while True:
    d = int(input('Day: '))
    m = int(input('Month: '))

    if d>1:
        d = d-1
        m = m
    elif d == 1 and m == 1:
        d = 31
        m = 12
    elif d == 1 and (m == 2 or m == 4 or m == 6 or m == 8 or m == 9 or m == 11):
        d = 31
        m = m - 1
    elif d == 1 and m == 3:
        d = 28
        m = m - 1
    elif d == 1 and (m == 5 or m == 7 or m == 10 and m == 12):
        d = 30
        m = m - 1
    else:
        print ('Error')

    print ('Day: ',d,'Month: ',m)
