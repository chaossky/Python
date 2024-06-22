# make a function that use only return statement
# check if input value is postive,negative, or zero.

def check_int(x):
    return ["positive", "negative", "zero"] [0 if x > 0 else 1 if x < 0 else 2]

print(check_int(-10))
print(check_int(0))
print(check_int(2))