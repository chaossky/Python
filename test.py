# In DNA strings, symbols "A" and "T" are complements of each other, 
# as "C" and "G". You function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. 
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"


def DNA_strand(dna):
    if len(dna) == 0:
        return ""
    if "A" in dna:
        dna = dna.replace("A", "T")
    elif "T" in dna:
        dna = dna.replace("T", "A")
    elif "C" in dna:
        dna = dna.replace("C", "G")
    elif "G" in dna:
        dna = dna.replace("G", "C")
        
    return dna
        
    
    