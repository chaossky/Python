from collections import deque

# de=deque(['name','age','DOB'])
# print(de)

dq=deque([10,20,30])

print(dq)

# Add element to the right
dq.append(40)
print(dq)

dq.appendleft(5)
print(dq)

dq.extend([50,60,70])
print(dq)

dq.extendleft([1,2,3])
print(dq)

dq.remove(20)
print(dq)

dq.pop()
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

dq.clear()
print(dq)