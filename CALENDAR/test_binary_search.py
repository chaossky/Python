import sys

def binary_search(arrays,search_value):
    length=len(arrays)
    low=0
    high=length-1
    mid=0

    while low<=high:
        mid=(low+high)//2
        if arrays[mid]==search_value:
            return mid
        elif arrays[mid]<search_value:
            low=mid+1
        elif arrays[mid]>search_value:
            high=mid-1
    return -1

def print_result(search_value,position, scores):
    if position != -1: 
        print(f"찾음 → 인덱스: {position}, 값: {scores[position]}") 
    else: 
        print(f"{search_value}는 리스트에 없음")

    
def main():
    scores=[10,20,30,40,50,70,85,90,100]
    search_value=40
    position=binary_search(scores,search_value)
    print_result(search_value,position,scores)
    
    print("-----------------------------")
    search_value=90
    position=binary_search(scores,search_value)
    print_result(search_value,position,scores)

if __name__=="__main__":
    main()