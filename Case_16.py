while True:
    yeah = int (input('Year: '))
    y = yeah%10

    if y == 0 or (y>=5 and y<=9):
        print (yeah,'лет')
    elif y == 1:
        print (yeah,'год')
    elif y>=2 and y<=4:
        print (yeah,'года')
    else:
        print ('smth wrng')
        
    
