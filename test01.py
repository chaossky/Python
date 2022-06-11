#make a pasword generator using pygame

import random

def password_generator(length):
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    numbers='0123456789'
    special_letters = '!@#$%^&*()_+'
    password = ''
    for i in range(length):
        password += random.choice(upper_case + lower_case + numbers + special_letters)
        
    # str1=random.choice(upper_case)
    # str2=random.choice(lower_case)
    # str3=random.choice(numbers)
    # str4=random.choice(special_letters)
    
    print(password)
    
password_generator(4)
password_generator(8)
password_generator(12)
    
    
    
    