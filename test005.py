# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. 
# Ignore letter case.

def is_isogram2(string):
    string =string.lower()
    if string == "":
        return True
    for i in string:
        if string.count(i) > 1:
            return False
    return True

def is_isogram(string):
    return len(string) == len(set(string.lower()))

# len함수는 문자열의 길이를 반환하는 함수이다.
# set은 집합 자료형을 만드는 것이다.
# 문자열의 길이와 문자열 안에 있는 알파벳 글자의 갯수를 세어서
# 차이가 있으면 False를 같으면 True를 반환하는 함수이다.
  
print(is_isogram("Dermatoglyphics"))
print(is_isogram("isogram"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
print(is_isogram("isIsogram"))
print(is_isogram(""))
