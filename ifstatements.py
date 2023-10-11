temperature=1
if temperature>30:
    print('It is a hot day') 
    print("Let's go swimming")
elif temperature>20: #(20,30]
    print("It's a nice day")
elif temperature>10: #(10,20]
    print("It's a cold day")
else:
     print("It's very cold")
