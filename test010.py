def check_int(x):
    return ['zero', 'positive', 'negative'][0 if x == 0 else 1 if x > 0 else 2]
print(check_int(10))
print(check_int(-10))
print(check_int(0))
