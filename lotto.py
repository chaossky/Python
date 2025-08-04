import random
for i in range(10):
    lotto_numbers = random.sample(range(1, 46), 6)
    lotto_numbers.sort()
    print("numbers are : ", lotto_numbers)
