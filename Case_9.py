import datetime

while True:
    d = int(input('Day: '))
    m = int(input('Month: '))
    date = datetime.date(2000, m, d)
    t = datetime.timedelta(days=1)
    print(date+t)
    

while True:
    d = int(input('Day: '))
    m = int(input('Month: '))

    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12) and d<31:
        m = m
        d = d+1
    elif (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10) and d == 31:
        m = m + 1
        d = 1
    elif m == 12 and d == 31:
        m = 1
        d = 1
    elif m == 2 and d<28:
        m = m
        d = d+1
    elif m == 2 and d == 28:
        m = 3
        d = 1
    elif (m == 4 or m == 6 or m == 9 or m == 11) and d<30:
        m = m
        d = d + 1
    elif (m == 4 or m == 6 or m == 9 or m == 11) and d == 30:
        m = m + 1
        d = 1
    else:
        print ('Error')

    print ('Day: ',d,'Month',m)
    
