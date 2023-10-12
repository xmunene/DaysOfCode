weight=input('Enter your weight: ')
unit=input('(K)g or (L)bs: ')
if unit.upper()=='K':
    convertion=float(weight)/0.45
    print('Your weight in lbs is: ',convertion)
else:
    convertion=float(weight)*0.45
    print('Your weight in kg is: ',convertion)
