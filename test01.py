#make a pasword generator using pygame

from operator import le
import random

def password_generator(length):
    """
    This function generates a random password of the specified length.  
    It returns the password as a string.
    """
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    numbers='0123456789'
    special_letters = '!@#$%^&*()_+'
    password = ''
    password += random.choice(upper_case)
    for i in range(length-4):
        password += random.choice(lower_case+numbers)
    for i in range(3):
        password += random.choice(special_letters)
    print(password)
    
for i in range(10):
    password_generator(12)
    

    
    
    
    