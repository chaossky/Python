# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100
# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(string):
    if string == '':
        return '1'
    else:
        if string[-1].isdigit(): 
            return string[:-1] + str(int(string[-1]) + 1)
        else:
            return string + '1'
        
print(increment_string('foo'))
print(increment_string('foobar23'))
print(increment_string('foo0042'))
print(increment_string('foo9'))
print(increment_string('foo099'))
print(increment_string(''))