import random

lower="abcdefghijklmnopqrstuvwxyz"
uppper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"

symbol="!@#"
# $%^&*()_`-=+[]{};':,./<>?"
all =lower+uppper+number+symbol
length=16

for i in range(10):
    password="".join(random.sample(all,length))
    print(password)

