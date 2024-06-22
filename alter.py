# Make a function that change the case of each character
# lowercase letter becomes uppercase, 
# uppercase becomes lowercase, 
# and other characters remain unchanged.

def alter(s):
    return s.swapcase()
    
str1="Hello World"
print(alter(str1))