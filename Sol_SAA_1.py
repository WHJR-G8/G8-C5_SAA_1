age = int(input("Enter a valid age: "))

if age < 0:
    print('Not a valid age')
    
elif 12 < age < 20:
    print('You are too young')
    
elif age == 20:
    print('You have just entered adulthood')
    
else:
    print('You are in the economical group')
