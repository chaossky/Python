import pickle

name='John'
age=20
address='123 Main St'
scores={'korean':40,'english':70,'math':60}

with open('john.p','wb') as file:
    pickle.dump(name,file)
    pickle.dump(age,file)
    pickle.dump(address,file)
    pickle.dump(scores,file)
    