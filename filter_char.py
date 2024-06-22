#create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_string(l):
    return [x for x in l if type(x) == int]

print(filter_string([1,2,3,'a','s','d']))
