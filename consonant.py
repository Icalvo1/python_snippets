## function that returns the consonants of a str ##
def anti_vowel(text):
    sto = ''
    for l in text:
        if l in 'aeiouAEIOU':
            print l  
        else:
            sto+= sto.join(l)
    return sto        
    
