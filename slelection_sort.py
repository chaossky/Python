def selection_sort(arr):
    #인덱스를 리스트의 길이만큼 정한다.
    for idx in range(len(arr)):
        #일단 최소값을 정한다. 
        min_idx = idx
        #다음 인넥스의 것 부터 끝까지 다시 
        for j in range(idx + 1, len(arr)):
            #만일 최소값하고 각각의 값을 비교하여 크면 값변화
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx] 
      
        
list1=[19,2,31,45,6,11,121,27]
selection_sort(list1)
print(list1)


# In[ ]