# Your task is to construct a building 
# which will be a pile of n cubes. 
# The cube at the bottom will have a volume of 
# n*n*n, the cube above will have volume of 
# (n−1)*(n−1)*(n−1) and so on until the top 
# which will have a volume of 1*1*1.
# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?
# Being given m and knowing the volume of a cube you can find the number of cubes you will have to build.
# The parameter of the function findNb will be an integer m and you have to return the integer n such as 
# n^3 + (n-1)^3 + ... + 1^3 = m if such a n exists or -1 if there is no such n.

def find_nb(m):
    n = 1
    while m > 0:
        m -= n**3
        n += 1
    return n-1 if m == 0 else -1

print(find_nb(4))
print (find_nb(16))
print(find_nb(4183059834009))