# given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

def alphabet_position(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = text.lower()
    output = ""
    for letter in text:
        if letter in alphabet:
            output += str(alphabet.index(letter) + 1) + " "
    #return output.strip()
    print(output.strip())
    
def alphabet_position2(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
    
alphabet_position("The sunset sets at twelve o' clock.")
str001=alphabet_position2("The sunset sets at twelve o' clock.")
print(str001)

