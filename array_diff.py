#My goal is to implement a difference funtion, which substract one list from another list and returns the result list.
#It should remove all values from list a, which are present in list b.
#array_diff([1,2],[1]) == [2]
#If a value is present in b, all of its occurrences must be removed from the other:
#array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    return [x for x in a if x not in b]

x1=[1,2,1,5,6,8,9]
x2=[1,2,5,9,10]

print(array_diff(x1,x2))

a1=['abc','b','c','d','e']
a2=['a','b','c']
print(array_diff(a1,a2))

