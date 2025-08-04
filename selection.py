#selection sort 

def selection_sort(arr):
    """
        we need to find the minimum value in the array and swap it 
        with the first element
        then we need to find the minimum value in the array and swap it
        with the second element
        then we need to find the minimum value in the array and swap it
        with the third element.....
        01. find the minimum value in the array
        02. 
        
    """ 
    
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

heights = [151,145,161,170,154,159,166,168,180,190]

order_heights = selection_sort(heights)

print(order_heights)