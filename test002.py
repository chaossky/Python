# Given a list and a number, 
# create a new list that contains 
# each number of list at most N times, 
# without reordering.

# For example if the input number is 2, 
# and the input list is [1,2,3,1,2,1,2,3], 
# you take [1,2,3,1,2], drop the next [1,2] 
# since this would lead to 1 and 2 being 
# in the result 3 times, and then take 3, 
# which leads to [1,2,3,1,2,3].
# With list [20,37,20,21] and number 1, 
# the result would be [20,37,21]

def delete_nth(order,max_e):
    result = []
    for i in order:
        if result.count(i) < max_e:
            result.append(i)
    return result

# keep this function call here  
# to see how to enter arguments in Python scroll down
list001= [1,2,3,1,2,1,2,3]
list002= [20,37,20,21]
print(list001.count(3))
print(list002.count(37))
print (delete_nth(list001,2)   ) 
print (delete_nth(list002,1)   )