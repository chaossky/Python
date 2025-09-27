import pickle

with open('john.p','rb') as file:
    name=pickle.load(file)
    age=pickle.load(file)
    address=pickle.load(file)   
    scores=pickle.load(file)
    
    print(name)
    print(age)
    print(address)
    for key,value in scores.items():
        print("{} score is {}".format(key,value))
    