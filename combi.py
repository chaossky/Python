### 제너레이터를 통해서 조합을 구현

def combinations_2(array,r):
    for i in range(len(array)):
        if r==1 : # 종료조건
            yield[array[i]]
        else:
            for next in combinations_2(array[i+1:],r-1):
                yield[array[i]]+next
                
               
for i in combinations_2([1,2,3,4],3):
    print(i,end=" ")
    
def ffactorial(integer):
    result=1
    for i in range(1,integer+1):
        result*=i
    return result

def fcombination(n,r):
    return ffactorial(n)//(ffactorial(r)*ffactorial(n-r))

def fpermutation(n,r):
    return ffactorial(n)//ffactorial(n-r)

print("result is : ",ffactorial(4))    
print("comb is ",fcombination(9,3))
print("permutation is ",fpermutation(9,3))  
