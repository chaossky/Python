#zip001.py -zip을 공부해 봅니다.

names=['Alice','Ben','Cain']
ages=[24,43,11]

people=dict(zip(names,ages))
print(people)
print("-----1-----")
print(list(people))
print(people['Alice'])
print("-----2-----")
for name,age in zip(names,ages):
    print(f"{name}'s age is {age} years old.")

#int(people['Alice'])
pairs=[('Alice',24),('Ben',43),('Cain',11)]
names,ages=zip(*pairs)
print("-----3-----")
print(names)
print(ages)


