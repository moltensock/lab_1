n = 10
match n:
    case 0: # if n == 0:
        print('it is 0')
    case 1: # elif n == 1:
        print('it is 1')
    case 10:
        print('it is 10')
    case _:
        print('not a number')