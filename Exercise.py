weight=input('Weight: ')
unit=input('(K)g or (L)bs: ')
if unit.upper()=="K":
    converted=float(weight)/0.45
    print('Weight in lbs is: ',converted)
else:
    converted=float(weight)*0.45
    print('Weight in kg is: ',converted)

