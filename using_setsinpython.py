import time

nums = list(range(10_000_000))
num_set = set(nums)

start = time.time()
9999999 in nums
print("List:", time.time() - start)

start = time.time()
9999999 in num_set
print("Set:", time. time() - start)

"""_summary_
    이 예제는 아주 많은 양의 데이타 셋을 처리할때 
    set을 사용하면 더 빠르다는 것을 보여주는 예제이다.
    
    보통 list내에서 어떤 객체 x가 있는지를 확인 하기 위해서
    if x in list : 와 같은 문법을 사용하곤 한다.
    
    데이타 셋이 클 경우 원하는 객체 x를 찾기 위해서  모든 데이타를 다 뒤져야 하며
    이는 검색 속도가 많으면 많을 수록 오래 걸린다.
    
    이럴때는 set으로 리스트를 바꿔 주면 훨씬 더 빠르게 처리할 수 있다.
    set은 해쉬테이블로 처리가 되므로 데이타셋이 커도 훨씬 더 빠르게 처리가 된다.
"""