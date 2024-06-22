# Given a string, you have to return a string in which each character
# (case-sensitive) is repeated once.

def double_char(s):
    return ''.join([x*2 for x in s] )

if __name__ == '__main__':
    print(double_char('Hello World'))
    
    print(double_char('abcd'))
    