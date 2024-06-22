A={1,2,3,4,5}
B={2,3,4,6,7}

#합집합
resultant_set=A|B
print("Union : ",resultant_set)

#교집합
resultant_set=A&B
print("Intersection : ",resultant_set)

#차집합
resultant_set=A-B
print("Difference : ",resultant_set)

#합집합-교집합
resultant_set=A^B
print("Symmetric Difference : ",resultant_set)

#부분집합인가?
resultant_set=A.issubset(B)
print("Subset : ",resultant_set)

#전체집합인가?
resultant_set=A.issuperset(B)
print("Superset : ",resultant_set)