# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
# The input string will only consist of lower case letters and/or spaces.
# 
# def getCount(inputStr):
#     return sum(1 for let in inputStr if let in "aeiouAEIOU")

def get_count(sentence):
    count=0
    for i in sentence:
        if i in "aeiou":
            count+=1
    return count

#or


def get_count1(sentence):
    count=0
    set001=set(sentence)
    vowel=["a","e","i","o","u"]
    for i in vowel:
        if i in set001:
            count+=1
    return count

print(get_count("abracadabra"))
print(get_count("hello"))