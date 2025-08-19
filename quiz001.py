def append_item(item, container=[]):
    container.append(item)
    return container

#explain the code
# This function appends an item to a list (container) that is initialized as an empty
# 
print(append_item(1),append_item(2), append_item(3))
#why does it return [1, 2]?
# The function `append_item` uses a mutable default argument (`container=[]`), 
# which means that the same list is used across multiple calls to the function.
#what does 'mutable' mean?
# Mutable means that the object can be changed after it is created. 
# In this case, the list can be modified by appending items to it.