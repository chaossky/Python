my_list = [["name", "age", "gender"], 
           ["John", "25", "male"], 
           ["Emily", "30", "female"], 
           ["Mike", "40", "male"]]
 
 
print(type(my_list))
 
# <class 'list'>

with open('my_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in my_list:
        writer.writerow(row)