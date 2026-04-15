import random

coin=['head','tail']
result=random.shuffle(coin)
head_no=0
tail_no=0

for i in range(10000):
    case=random.choice(coin)
    if case=='head':
        head_no=head_no+1
    else:
        tail_no=tail_no+1
        
print("HEAD IS : ", head_no,"TAIL IS : ",tail_no)
    