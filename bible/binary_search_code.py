def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        
        if arr[mid]==target:
            return mid #found the target, return its index
        elif arr[mid]<target:
            left=mid+1 #Search right half
        else:
            right=mid-1 #search left half
    return -1   #target not found

def binary_search_recursive(arr,target,left,right):
    if left>right:
        return -1 #target not found
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search_recursive(arr,target,mid+1,right)
    else:
        return binary_search_recursive(arr,target,left,mid-1)


numbers=[3,8,15,23,42,56]
target=23

result=binary_search(numbers,target)

if result!=-1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")    