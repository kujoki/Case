while True:
    A = int(input('Введите год: '))

    y = (A - 1984)/12
    m = y / 60
    print (m)
    m_y = m/12
    print (m_y)

    if m == 0:
        if 0<=y<=1:
            print ('зеленый')
        elif 1<y<=2:
            print ('красный')
        elif 2<y<=3:
            print ('желтый')
        elif 3<y<=4:
            print ('белый')
        elif 4<y<=5:
            print ('черный')
    else:
        if 0<=m_y<=1:
            print ('зеленый')
        elif 1<m_y<=2:
            print ('красный')
        elif 2<m_y<=3:
            print ('желтый')
        elif 3<m_y<=4:
            print ('белый')
        elif 4<m_y<=5:
            print ('черный')
        
        
